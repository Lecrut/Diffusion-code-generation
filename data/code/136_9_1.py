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
    a1 = True
    b1 = True
    result1 = calculator.logical_operation(a1, b1)
    print(f"Inputs: a={a1}, b={b1}, Result: {result1}")
    a2 = True
    b2 = False
    result2 = calculator.logical_operation(a2, b2)
    print(f"Inputs: a={a2}, b={b2}, Result: {result2}")
    a3 = False
    b3 = False
    result3 = calculator.logical_operation(a3, b3)
    print(f"Inputs: a={a3}, b={b3}, Result: {result3}")
    a4 = False
    b4 = True
    result4 = calculator.logical_operation(a4, b4)
    print(f"Inputs: a={a4}, b={b4}, Result: {result4}")