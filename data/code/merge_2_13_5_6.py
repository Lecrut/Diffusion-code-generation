def safe_max(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        max_val = values[0]
        for item in values[1:]:
            try:
                max_val = max(max_val, item)
            except TypeError:
                raise ValueError(f"Cannot compare values of different types: {type(max_val)} and {type(item)}")
        return max_val
    except IndexError:
        pass
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
if __name__ == '__main__':
    test_cases = [
        [], 
        [10], 
        [-5, 3.7, -2], 
        ["apple", "banana"],                                                                                                                                                                                                                                                             
    ]
    results = []
    try:
        for i, case in enumerate(test_cases):
            result = safe_max(case)
            results.append(f"Case {i}: Input={case}, Max={result}")
    except Exception as e:
        results.append(f"Error in case: {e.args[0]}")
    print("\n".join(results))