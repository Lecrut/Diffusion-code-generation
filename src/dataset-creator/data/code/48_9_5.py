def divide_numbers(initial: float, divisor: float) -> tuple[float, str]:
    if divisor == 0:
        return initial, "Error"
    try:
        result = initial / divisor
        return result, "Success"
    except Exception as e:
        return float('nan'), f"{e}"
if __name__ == '__main__':
    init_val = 10.5
    div_val = 2
    final_result, status = divide_numbers(init_val, div_val)
    if status != "Error":
        print(f"Result: {final_result}")