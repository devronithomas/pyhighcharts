"""
Author: Roni Thomas
email: ronithomas10@gmail.com
email2: dev.ronithomas@gmail.com
Date: 02/12/2021
"""

class HighChart:
    
    """
    `name= lst` list of strings --> name of the legends
    `data = lst` list of lists --> data to be plotted
    NOTE: `len(name) == len(data)`

    `container: str` string --> id of the container, default: "container-1"
  
    All features are addded to their respective dictonary and combined together
    in main dictonary, which is then saved as javascript code. \n
    'args' format: \n
    `args.get('user entered value', 'default value')`

    #### Chart Selection:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | chart type | `chart = str` | line |

    #### Adding Titles:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | title | `title = str` | None |
    | subtitle | `subtitle = str` | None |
    | y-axis title | `ytitle = str` | None |
    | x-axis title | `xtitle = str` | None |

    #### Definining start point of x-axis:
    Default start point for x-axis is 0.
    To change start point, use:
    `xpointStart = int`

    #### Tooltip:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | tooltipShared | `tooltipShared = bool` | false |
    | tooltipvalueSuffix | `tooltipvalueSuffix = str` | None |

    #### Legend:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | enableLegend | `enableLegend = bool` | true |
    | legendLayout | `legendLayout = str` | vertical |
    | legendHorizontalAlign | `legendHorizontalAlign = str` | right |
    | legendVerticalAlign | `legendVerticalAlign = str` | middle |

    #### Vertical Plot Bands:
    call `HighCharts.plotBands(start, end, color)`
    `start` and `end` are integers, `color` is a string.
    eg: `HighCharts.plotBands(3, 4, 'rgba(255, 0, 217, 0.2)')`

    #### Width:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | maxWidth | `maxWidth = int` | 500 |

    #### Credits:
    | Feature | Syntax | Default Value |
    | ------ | ------ | ------ |
    | credits | `credits = bool` | false |
    | creditsText | `creditsText = str` | None |
    """
    def __init__(self, name:list, data:list, container="container-1", **args):
        self.name = name
        self.data = data
        self.container = container
        self.args = args
        self.layout = {}
        self.chartType()
        self.globalFeature()
        self.series()

    def updateLayout(self, dict):
        self.layout.update(dict)

    #chart type
    def chartType(self):
        chart = {'chart': {
            'type':self.args.get('chart', '')
        }}
        self.updateLayout(chart)

    def globalFeature(self):
        globalFeatures = {
        #title
        "title":{
            "text":self.args.get('title', '')
        },
        #subtitle
        "subtitle":{
            "text":self.args.get('subtitle', '')
        },
        #y-axis title
        "yAxis":{
            "title":{
                "text":self.args.get('ytitle', '')
            }
        },
        #x-axis title
        "xAxis":{
            "title":{
                "text":self.args.get('xtitle', '')
            },
            "plotBands":[]
        },
        "plotOptions":{
        "series":{
            "label":{
                "connectorAllowed": "false"
            },
            "pointStart":self.args.get('xpointStart', 0)
            }
        },
        #tooltip
        "tooltip": {
            "shared":self.args.get('tooltipShared', 'false'),
            "valueSuffix":self.args.get('tooltipvalueSuffix', '')
        },
        #legend
        "legend":{
            "enabled":self.args.get('enableLegend', 'true'),
            "layout":self.args.get('legendLayout', 'vertical'),
            "align":self.args.get('legendHorizontalAlign', 'right'),
            "verticalAlign":self.args.get('legendVerticalAlign', 'middle')
        },
        #credits
         "credits": {
            "enabled":self.args.get('credits', 'false'),
            "text":self.args.get('creditsText', '')
        },
        #responsive
        "responsive":{
            "rules":[{
                "condition":{
                    "maxWidth":int(self.args.get("maxWidth", "500"))
                },
                "chartOptions":{
                    "legend":{
                        "layout":self.args.get("chartLayout", "horizontal"),
                        "align":self.args.get("chartAlign","center"),
                        "verticalAlign":self.args.get("verticalAlign", "bottom")
                    }
                }
            }]
        }  
        }

        self.updateLayout(globalFeatures)

    def plotBands(self, start:int, end:int, color:str):
        plotBand = {
          "from": int(start),
          "to": int(end),
          "color": color
            }
        self.layout['xAxis']['plotBands'].append(plotBand)
    
    def series(self):
        #iteration for waves to be plotted
        series = {"series":[]}
        for n, d in zip(self.name,self.data):
            series["series"].append({"name":n, "data":d})

        self.updateLayout(series)


    #adding highchart preffix to call highchart function in js
    def savehighchart(self, filename:str = 'charts'):
        final = f"Highcharts.chart('{self.container}', {self.layout});"

        with open(f'{filename}.js', 'a') as file:
            file.write(final)

