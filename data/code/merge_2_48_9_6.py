import sys
def divide_numbers(initial: float, divisor: float) -> tuple[float | None]:
    if not isinstance(divisor, (int, float)):
        return None
    try:
        result = initial / divisor
        return result
    except ZeroDivisionError:
        return None
if __name__ == '__main__':
    INITIAL_VALUE = 100.5
    DIVISOR_VALUE = 2.375
    final_result = divide_numbers(INITIAL_VALUE, DIVISOR_VALUE)
    if isinstance(final_result, float):
        print(f"Result: {final_result}")