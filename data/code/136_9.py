class BooleanCalculator:
    def logical_operation(self, a: bool, b: bool) -> str:
        if a and b:
            return "Both inputs are True, so the result is True."
        elif a or b:
            return "At least one input is True, so the result is True."
        else:
            return "Both inputs are False, so the result is False."
if __name__ == '__main__':
    calculator = BooleanCalculator()
    print(calculator.logical_operation(True, True))
    print(calculator.logical_operation(True, False))
    print(calculator.logical_operation(False, True))
    print(calculator.logical_operation(False, False))