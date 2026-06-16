def safe_max(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        return max(values)
    except ValueError as e:
        if "uncomparable types" in str(e).lower():
            unique_types = set(type(x).__name__ for x in values if not isinstance(x, (list, tuple)))
            raise TypeError(f"Mixed uncomparable types found: {unique_types}") from None
    except Exception as e:
        raise RuntimeError("Unexpected error during max computation") from e
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        (5,),
        [-10, -20, -30],
        ["apple", "banana"],
    ]
    for i, data in enumerate(test_cases):
        try:
            result = safe_max(data)
            print(f"Test case {i}: Input={data}, Max={result}")
        except Exception as ex:
            print(f"Test case {i} Error: {ex.__class__.__name__}: {ex}")