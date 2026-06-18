from typing import Union
def calculate_quotient(dividend: float, divisor: float) -> float:
    try:
        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both operands must be numeric types.")
        result = dividend / divisor
        return result
    except ZeroDivisionError as e:
        print(f"Zero division error occurred: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {type(e).__name__}: {e}")
        raise
if __name__ == '__main__':
    sample_dividend = 10.5
    sample_divisor = 2
    try:
        quotient_result = calculate_quotient(sample_dividend, sample_divisor)
        print(f"The result of dividing {sample_dividend} by {sample_divisor} is: {quotient_result}")
    except ZeroDivisionError as e:
        print("Calculation failed due to division by zero.")
    except Exception as e:
        print("An error occurred during calculation.")