def divide_numbers(initial: float, divisor: float) -> tuple[float, str]:
    if divisor == 0:
        return initial, "Division by zero error"
    result = initial / divisor
    try:
        remainder = abs(result - round(result)) * abs(divisor)
        is_integer_result = (initial % divisor == 0 or isinstance(initial, int) and isinstance(divisor, int) and initial % divisor == 0)
        if not is_integer_result:
            return result, "Non-integer division"
        else:
            return round(result), "Integer division successful"
    except Exception as e:
        return float('nan'), str(e)
if __name__ == '__main__':
    initial_value = 10.5
    divisor_value = 2
    result, message = divide_numbers(initial_value, divisor_value)
    print(f"{result} | {message}")