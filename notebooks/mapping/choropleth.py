import mapclassify

schemes = ['Quantiles', 'Equal_Interval', 'Maximum_Breaks', 'Fisher_Jenks']
dispatcher = {}
for scheme in schemes:
    dispatcher[scheme.lower()] = eval('mapclassify.classifiers.{scheme}'.format(scheme=scheme))

def choropleth(df, column, scheme='Quantiles', k=5, cmap='BuGn', legend=False,  \
               edgecolor='black', linewidth=0.1, alpha=0.75, ax=None, label_int=False):
    """
    Choropleth mapping based on geopandas and pysal2.0rc
    
    Parameters
    ----------
    
    df: geopandas GeoDataFrame
    
    column: string
            column name for attribute that is to be mapped
            
    scheme: string
            Name of mapclassify classification scheme
            
    k:  int
        number of classes for choropleth
        
    cmap: string
          name of colormap from matplotlib
          
    legend: Boolean
            Show legend (True)
            
    edgecolor: string
             Color of polygon edges
    
    linewidth: float
            width of edges
            
    alpha: float
           transparency
            
    ax: matplotlib.pyplot plt axis
    
    label_int: If True legend values are set to ints, otherwise geopandas default
    
    
    """
    classified = dispatcher[scheme.lower()](df[column], k=k)
    legend = [ cut  for cut in classified.bins]
    labels = [classified.bins[ybi] for ybi in classified.yb]
    if label_int:
        labels = [int(label) for label in labels]
    ax = df.assign(cl=labels).plot(column='cl', categorical=True, \
                                   cmap=cmap, legend=legend, 
                                   edgecolor=edgecolor, linewidth=linewidth, \
                                   alpha=alpha, ax=ax)
    return ax
    
