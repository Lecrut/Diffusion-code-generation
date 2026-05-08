class BooleanCalculator:
    def logical_operation(self, a: bool, b: bool) -> str:
        result = a and b
        return f"Logical AND of {a} and {b} is {result}"
if __name__ == '__main__':
    calculator = BooleanCalculator()
    bool1 = True
    bool2 = False
    result_and = calculator.logical_operation(bool1, bool2)
    print(result_and)
    bool3 = True
    bool4 = True
    result_or = calculator.logical_operation(bool3, bool4)
    print(result_or)
    bool5 = False
    bool6 = False
    result_xor = calculator.logical_operation(bool5, bool6)
    print(result_xor)