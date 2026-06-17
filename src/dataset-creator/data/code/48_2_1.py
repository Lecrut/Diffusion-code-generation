def safe_divide(a: float, b: float) -> float | None:
    try:
        if b == 0:
            return None
        result = a / b
        return round(result, 2)
    except (TypeError, ZeroDivisionError):
        return None
if __name__ == '__main__':
    num1_str = "45"
    num2_str = "3.0"
    try:
        first_num = float(num1_str)
        second_num = float(num2_str)
        result = safe_divide(first_num, second_num)
        if result is not None:
            print(f"{first_num} / {second_num} = {result}")
        else:
            print("Error occurred during division.")
    except ValueError as ve:
        print(f"Invalid input format: {ve}")