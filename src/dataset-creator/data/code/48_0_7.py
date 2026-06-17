def divide_numbers(a: float, b: float) -> str:
    if a is None or b is None:
        return "Error: Input values cannot be null."
    try:
        num_a = float(a)
        num_b = float(b)
        if not (isinstance(num_a, (int, float)) and isinstance(num_b, (int, float))):
            return "Error: Inputs must be numeric types."
        if b == 0.0 or abs(b) < 1e-9:
            return "Error: Division by zero is undefined."
        result = num_a / num_b
        if isinstance(num_a, int) and isinstance(num_b, (int, float)) and not math.isclose(result, round(result)):
            result_str = f"{result:.6f}"
        else:
            result_str = str(int(round(result)))
    except ValueError as ve:
        return f"Error: Invalid input format. {ve}."
    return f"Result of dividing {num_a} by {num_b}: {result_str}"
import math
if __name__ == '__main__':
    sample_values = [10, 2]
    result_message = divide_numbers(sample_values[0], sample_values[1])
    print(result_message)