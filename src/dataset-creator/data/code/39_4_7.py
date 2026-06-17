def find_largest_value(numbers: list[float]) -> float | None:
    if len(numbers) == 0:
        return None
    try:
        max_val = numbers[0]
        for num in numbers[1:]:
            if not isinstance(num, (int, float)):
                raise ValueError(f"Invalid data type '{type(num).__name__}' found at index {numbers.index(num)}")
            if num > max_val:
                max_val = num
        return max_val
    except IndexError as e:
        raise ValueError("List access failed due to invalid indexing or unexpected structure.") from e
if __name__ == '__main__':
    test_cases = [
        {
            'input': [-5, 10, -2.5, 3],
            'expected_output': 10.0
        },
        {
            'input': [],
            'expected_output': None
        },
        {
            'input': [42],
            'expected_output': 42.0
        }
    ]
    for i, case in enumerate(test_cases):
        print(f"Test Case {i + 1}:")
        try:
            result = find_largest_value(case['input'])
            if isinstance(result, float) and (result == int or not result.is_integer()):
                formatted_result = f"{result}" if case['expected_output'] is None else str(float(int(round(result)))) if result != 42.0 else "None"
            print(f"Input: {case['input']}")
            print(f"Output: {result}")
        except ValueError as ve:
            print(f"Error occurred for input {case['input']}: {ve}")