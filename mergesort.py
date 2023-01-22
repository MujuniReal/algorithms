class Sorter:
    def __init__(self,raw_list,):
        self.rawList = raw_list
        self.sortedList = self.mergesort(rawList=self.rawList)

    def mergesort(self,rawList):
        rawListLength = len(rawList)
        sortedList = []
        if rawListLength == 1:
            return rawList

        halfLen = int(rawListLength / 2)

        leftNos = rawList[:halfLen]
        rightNos = rawList[halfLen:]

        sortedLeft = self.mergesort(leftNos)
        sortedRight = self.mergesort(rightNos)

        leftCounter = 0
        rightCounter = 0

        for i in range (0,rawListLength):
            lenSrtRight = len(sortedRight)
            lenSrtLeft = len(sortedLeft)
            if rightCounter == lenSrtRight or leftCounter == lenSrtLeft:
                if rightCounter == lenSrtRight:
                    sortedList.insert(i,sortedLeft[leftCounter]) 
                    leftCounter += 1
                else:
                    sortedList.insert(i,sortedRight[rightCounter])
                    rightCounter += 1

            else:
                if sortedLeft[leftCounter] > sortedRight[rightCounter]:
                    sortedList.insert(i,sortedRight[rightCounter])
                    rightCounter += 1
                else:
                    sortedList.insert(i,sortedLeft[leftCounter])
                    leftCounter += 1

        return sortedList


disOrganisedList = [2,3,5,7,8,9,0,1,99]

sortObj = Sorter(raw_list=disOrganisedList)

print(sortObj.sortedList)
