
def bubbleSort(args):
    for i in range(1,len(args)):
        for j in range(0,len(args)-i):
            if (args[j]>args[++j]):
                args[j],args[j+1]=args[j+1],args[j]
    return args;
            
    