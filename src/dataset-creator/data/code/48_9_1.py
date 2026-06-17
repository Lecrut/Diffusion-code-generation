def divide_numbers(initial: float, divisor: float) -> tuple[float, str]:
    try:
        result = initial / divisor
        return result, "Success"
    except ZeroDivisionError:
        return 0.0, "Divisor is zero"
if __name__ == '__main__':
    init_val = 100.5
    div_val = 2.3
    final_result, status_message = divide_numbers(init_val, div_val)
    print(f"{status_message}: {final_result}")