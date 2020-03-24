line_chart_utterances = ["[x_axis] over [y_axis]", 
                         "how does [y_axis] change with [x_axis]", 
                         "[y_axis] as a function of [x_axis]", "line chart showing [y_axis] over [x_axis]"]
line_chart_type_signature = {"x_axis": "quantitative|temporal|nominal", 
                             "y_axis": "quantitative", 
                             "symbol": "ordinal|nominal|quantitative"}
line_chart_info = {"utterances": line_chart_utterances, 
                   "types": line_chart_type_signature}

def create_line_chart(x_axis, y_axis, symbol=None): 
    if symbol is None: 
        chart = alt.Chart(source).mark_line().encode(
        x=x_axis,
        y=y_axis,
        )
    else: 
        chart = alt.Chart(source).mark_line().encode(
            x=x_axis,
            y=y_axis,
            color=symbol 
        )
    return chart



bar_chart_utterances = ["breakdown of [x_axis] by [y_axis]", 
                        "bar chart showing [y_axis] with respect to [x_axis]"]
bar_chart_type_signature = {"x_axis": "ordinal|nominal|quantitative", 
                            "y_axis": "quantitative"}
bar_chart_info = {"utterances": bar_chart_utterances, 
                  "types": bar_chart_type_signature}

def create_bar_chart(x_axis, y_axis): 
    chart = alt.Chart(source).mark_bar().encode(
        x=x_axis, 
        y=y_axis, 
    )
    return chart



reference = {"location": ("lat", "long")}
geographical_heatmap_type_signature = {"lat": "quantitative", 
                                       "long": "quantitative", 
                                       "symbol": "quantitative|ordinal|nominal"}
geographical_heatmap_info = {"utterances": ["frequency of [symbol] by [location]"], 
                             "reference": reference, 
                             "types": geographical_heatmap_type_signature}

def create_geographical_heatmap(lat, long, symbol): 
    return 



strip_chart_utterances = []
strip_chart_type_signature = {}
strip_chart_info = {"utterances": strip_chart_utterances, 
                    "types": strip_chart_type_signature}

def create_strip_chart(): 
    return 



scatter_plot_utterances = []
scatter_plot_type_signature = {}
scatter_plot_info = {"utterances": scatter_plot_utterances, 
                     "types": scatter_plot_type_signature}

def create_scatter_plot(): 
    return 



histogram_utterances = []
histogram_type_signature = {}
histogram_info = {"utterances": histogram_utterances, 
                  "types": histogram_type_signature}

def create_histogram(): 
    return 



forecast_utterances = []
forecast_type_signature = {}
forecast_info = {"utterances": forecast_utterances, 
                 "types": forecast_type_signature}

def time_series_forecast(data, prediction_interval): 
    m = Prophet()
    m.fit(data)
    future = m.make_future_dataframe(periods=prediction_interval)
    forecast = m.predict(future)
    fig = m.plot(forecast)
    return fig



program_annotations = {"line chart": {"function": create_line_chart, "info": line_chart_info}, 
                       "bar chart": {"function": create_bar_chart, "info": bar_chart_info},
                       "geographical heatmap": {"function": create_geographical_heatmap, "info": geographical_heatmap_info},
                       "strip chart": {"function": create_strip_chart, "info": strip_chart_info},
                       "scatter plot": {"function": create_scatter_plot, "info": scatter_plot_info},
                       "histogram": {"function": create_histogram, "info": histogram_info},
                       "time series forecast": {"function": time_series_forecast, "info": forecast_info},
                       }