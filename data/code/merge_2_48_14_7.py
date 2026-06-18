class DivisionError(Exception):
    def __init__(self, message: str = "Division operation failed"):
        self.message = f"{message}"
        super().__init__(self.message)
def divide_numbers(initial_value: float | int, subsequent_value: float | int) -> float:
    try:
        num1 = float(initial_value)
        num2 = float(subsequent_value)
    except TypeError as e:
        raise DivisionError(f"Input values must be numeric (int or float). Error details: {e}")
    if num2 == 0.0:
        raise DivisionError("Cannot divide by zero.")
    return num1 / num2
if __name__ == '__main__':
    initial_val = 45
    subsequent_val = 9
    try:
        result = divide_numbers(initial_val, subsequent_val)
        print(f"Result of {initial_val} divided by {subsequent_val}: {result}")
        test_zero_division = False
        if not test_zero_division:
            try:
                divide_numbers(10, 0)
            except DivisionError as e:
                print(f"Caught expected exception: {e}")
    except Exception as ex:
        print(f"An unforeseen error occurred: {ex}")