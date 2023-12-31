import numpy as np

def solveDict(solveList):
    solveDict = {}
    for i in range(0, len(solveList),2):
        solveDict[solveList[i]] = solveList[i+1]
    return solveDict

def listDict(solveDict):
    listDict = {}
    dnf = "DNF"
    DNF = "1000000"
    for key, value in solveDict.items():
        listDict[key] = value.replace(dnf, DNF).split()
    return listDict

def intList(listDict):
    intList = {}
    for key, value in listDict.items():
        intList[key] = list(map(float, value))
    return intList

def fastest(intList):
    fastest = {}
    for key, value in intList.items():
        fastest[key] = min(value)
    return fastest

def slowest(intList):
    initSlowest = {}
    slowest = {}
    for key, value in intList.items():
        initSlowest[key] = max(value)
    for key, value in initSlowest.items():
        if value == 1000000.0:
            slowest[key] = "DNF"
        else:
            slowest[key] = value
    return slowest, initSlowest

def new_intList(intList, fastest, initSlowest):
    new_intList = {}
    for key, values in intList.items():
        copy_values = values[:]
        for value in values:
            if value in fastest.values() or value in initSlowest.values():
                copy_values.remove(value)
        new_intList[key] = copy_values
    return new_intList

def mean(new_intList):
    mean = {}
    meanValues = []
    for key, values in new_intList.items():
        mean[key] = np.mean(values)
    return mean

def sort_mean(mean):
    copy_mean = mean.copy()
    sort_mean = {}
    while len(copy_mean) != 0:
        fst_ave_key = min(copy_mean, key=copy_mean.get)
        sort_mean[fst_ave_key] = copy_mean[fst_ave_key]
        del copy_mean[fst_ave_key]
    return sort_mean
