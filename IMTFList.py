# Silvio Orozco Vizquerra
# Universidad del Valle de Guatemala
# Analisis de Algoritmos 

#Implementation of IMoveToFrontList
import pandas as pd  #To print easily our results

#Implementation of IMoveToFrontList
class IMoveToFrontList:
    def __init__(self, initialConfig=[0,1,2,3,4]):
        self.listConfig = initialConfig
    
    def __str__(self):
        return str(self.listConfig)

    def insertItem(self,item):
        self.listConfig.append(item)
        return self.listConfig
    
    def searchItem(self,item,indexSearch,searchList):
        initConfig = self.listConfig
        index = self.listConfig.index(item)
        cost = index + 1
        finalConfig = initConfig
        if(self.listConfig[index] in searchList[indexSearch+1:indexSearch+index+1]):
            finalConfig=[initConfig[index]] + initConfig[0:index] + initConfig[(index+1):len(initConfig)]
        self.listConfig = finalConfig
        return initConfig,index,cost,finalConfig

    def searchListOfItems(self,searchList):
        totalCost = 0 
        initConfigs=[]
        indexes=[]
        costs=[]
        finalConfigs=[]
        for indexSearch in range(len(searchList)):
            item = searchList[indexSearch]
            initConfig,index,cost,finalConfig = self.searchItem(item,indexSearch,searchList)
            initConfigs.append(str(initConfig))
            indexes.append(index)
            costs.append(cost)
            finalConfigs.append(str(finalConfig))
            totalCost = totalCost + cost
        df = pd.DataFrame({"Search Elem":searchList,"Initial Config":initConfigs,"Found Index":indexes,"Cost":costs,"Final Config":finalConfigs})  
        print(df)
        print(f'Total Cost {totalCost}')
            

mtf = IMoveToFrontList()
print(mtf)
searchList=[0, 1, 2, 3, 4,0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
mtf.searchListOfItems(searchList)
