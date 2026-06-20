class ComplexScenarioTest:
    STR1 = "apple"
    STR2 = "apple"
    STR3 = "banana"
    NUM1 = 10
    NUM2 = 15
    NUM3 = 10

    @staticmethod
    def check_conditions():
        condition1 = (ComplexScenarioTest.STR1 == ComplexScenarioTest.STR2)
        condition2 = (ComplexScenarioTest.STR1 != ComplexScenarioTest.STR3)
        condition3 = (ComplexScenarioTest.NUM1 < ComplexScenarioTest.NUM2)
        condition4 = (ComplexScenarioTest.NUM1 == ComplexScenarioTest.NUM3)

        return condition1 and condition2 and condition3 and condition4

    @staticmethod
    def run_test():
        if ComplexScenarioTest.check_conditions():
            print("All conditions met.")
        else:
            print("One or more conditions failed.")

if __name__ == '__main__':
    ComplexScenarioTest.run_test()