class ComplexScenario:
    def __init__(self):
        self.str1 = "apple"
        self.str2 = "apple"
        self.str3 = "banana"
        self.num1 = 10
        self.num2 = 15

    def check_conditions(self):
        condition1 = (self.str1 == self.str2)
        condition2 = (self.str1 != self.str3)
        condition3 = (self.num1 < self.num2)
        return condition1 and condition2 and condition3

if __name__ == '__main__':
    scenario = ComplexScenario()
    if scenario.check_conditions():
        print("All conditions met.")
    else:
        print("One or more conditions failed.")