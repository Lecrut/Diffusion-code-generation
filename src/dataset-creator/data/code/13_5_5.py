def safe_max(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Input must be a list or tuple")
    try:
        return max(values)
    except ValueError as e:
        if "uncomparable types" in str(e).lower():
            raise TypeError(f"Mixed uncomparable types found in sequence. Valid values provided: {values}") from None
        else:
            raise
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        (5,),
        [-10, -5, 0, 10],
    ]
    results = []
    for i, data in enumerate(test_cases):
        try:
            res = safe_max(data)
            results.append((i, "Success", res))
        except Exception as ex:
            results.append((i, f"Error: {type(ex).__name__}", str(ex)))
    print("Execution Results:")
    for idx, status, msg in results:
        if isinstance(msg, tuple):
            print(f"Case {idx}: Status={status}, Value={msg[2]}")
        else:
            print(f"Case {idx}: Status={status}, Message={msg}")