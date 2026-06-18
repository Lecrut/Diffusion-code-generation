import sys
def divide_numbers(initial: float, divisor: float) -> tuple[float | None]:
    if not isinstance(divisor, (int, float)):
        raise TypeError("Divisor must be a number")
    try:
        result = initial / divisor
        return [result]
    except ZeroDivisionError:
        return [None]
if __name__ == '__main__':
    INITIAL_VAL = 100.5
    DIVISOR_VAL = 4
    output_list = divide_numbers(INITIAL_VAL, DIVISOR_VAL)
    if isinstance(output_list[0], float):
        print(f"Result: {output_list[0]}")
    else:
        print("Error: Division by zero or invalid input.")