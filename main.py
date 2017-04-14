class Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    def printNumInstances():
        print(" Spam NUmber of instances:",Spam.numInstance)
    printNumInstances = staticmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances():
        print ("Extra:stuff...")
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

class Other(Spam):pass

a = Sub()
b = Sub()

a.printNumInstances()
Sub.printNumInstances()
Spam.printNumInstances()

c = Other()
c.printNumInstances()
Other.printNumInstances()


#result as fallow:
# Extra:stuff...
# (' Spam NUmber of instances:', 2)
# Extra:stuff...
# (' Spam NUmber of instances:', 2)
# (' Spam NUmber of instances:', 2)
# (' Spam NUmber of instances:', 3)
# (' Spam NUmber of instances:', 3)







