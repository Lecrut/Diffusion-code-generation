def process_input(value):
    if isinstance(value, (int, float)):
        try:
            num = float(value)
            if -10 <= num <= 10:
                return f"Value {num} is within the safe range [-10, 10]."
            elif num < -10 or num > 10:
                return f"Warning: Value {num} exceeds the safe limits."
        except ValueError as ve:
            raise TypeError(f"Invalid number format provided. Error details: {ve}") from ve
    else:
        return "Error: Input must be a numeric value (int or float)."
if __name__ == '__main__':
    test_cases = [0, 10.5, -9, -20, 'abc', None, '', True]
    results = []
    for case in test_cases:
        try:
            result = process_input(case)
            results.append((case, result))
        except Exception as e:
            results.append((f"Failed on {type(case).__name__}", f"Exception occurred: {e}"))
    print("Processing Results:")
    for input_val, output in results:
        if isinstance(input_val, str):
            print(f"[{input_val}] -> {output}")
        else:
            print(f"Input: {input_val!r} | Result: {output}")