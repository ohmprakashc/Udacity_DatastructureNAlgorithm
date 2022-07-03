"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    
    def __init__(self):
        self.Classiness=0
        self.items = []
        """
        print ("I am in init", \
               "Classiness =", self.Classiness, \
               "Items =", self.items)
        """
   
    def getClassiness(self, *args):
        
        #print ("I am in getClassiness", *args)
        #args is Tuple. Converting it to List
        argsToList=[*args]
        #print (argsToList, len(argsToList))
        
        y=len(argsToList)
        
        #print ("Printing numer of args",y)
        
        for i in range(y):
            #print ("I am in for loop, loop number", i, y)
            if argsToList[i]=="tophat":
                #print ("I am in tophat-", argsToList[i])
                self.Classiness=int(self.Classiness)+2
                #print ("I am in tophat. Classiness=", self.Classiness)
                
            elif args[i]=="bowtie":
                #print ("I am in bowtie-", argsToList[i])
                self.Classiness=int(self.Classiness)+4
                #print ("I am in bowtie. Classiness=", self.Classiness)
                
            elif  argsToList[i]=="monocle":
                #print ("I am in monocle-", argsToList[i])
                self.Classiness=int(self.Classiness)+5
                #print ("I am in monocle. Classiness=", self.Classiness)
                
            else:
                self.Classiness=self.Classiness+0
                #print ("else statement")
                #print (self.Classiness)
                
            #return self.Classiness
        #print ("Current Classiness inside getClassiness=",self.Classiness)
        return self.Classiness
            
    def addItem(self, Item):
        self.Classiness=0
        #print ("Reset classiness=0")
        self.items.append(Item)
        #print ("I am in addItem", self.items)
        passItemArray=self.items
        self.getClassiness(*passItemArray)
        
# Test cases
me = Classy()

# Should be 0
print ("Classiness=", me.getClassiness())

me.addItem("tophat")
print ("Added tophat",me.getClassiness())

me.addItem("bowtie")
print ("Added bowtie",me.getClassiness())

me.addItem("jacket")
print ("Added jacket",me.getClassiness())

me.addItem("monocle")
print ("Added monocle",me.getClassiness())

me.addItem("bowtie")
print ("Added bowtie",me.getClassiness()
