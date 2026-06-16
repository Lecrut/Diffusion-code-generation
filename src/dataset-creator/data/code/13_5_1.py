def safe_max(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        return max(values)
    except ValueError as e:
        if "uncomparable types" in str(e).lower():
            unique_types = set(type(x).__name__ for x in values)
            msg = f"Mixed uncomparable types detected: {unique_types}"
            raise TypeError(msg) from None
        else:
            raise
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        (4, 5),
        ["a", "b"],
        [[1, 2], [3]],                                                                                                                                                                                                                                                                                                                                                  
        [1, "one", 2],                                                                                                                                                                                                                                   
    ]
    results = []
    for i, data in enumerate(test_cases):
        try:
            res = safe_max(data)
            results.append((i, "Success", res))
        except Exception as ex:
            results.append((i, f"Error: {type(ex).__name__}", str(ex)))
    print("Test Results:")
    for idx, status, msg in results:
        if isinstance(msg, tuple):                                                                             
             pass 
        else:
            print(f"Case {idx}: {status} -> {msg}")