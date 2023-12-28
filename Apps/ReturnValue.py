
class ReturnValue():
    def initialize(self):
        self.log("do dah!")

    def addNum(self, num1, num2):
        return num1 + num2
    

test = ReturnValue()
print(test.addNum(1,2))