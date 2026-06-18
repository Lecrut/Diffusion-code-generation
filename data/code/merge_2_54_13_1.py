import sys
def get_midpoint_index(data):
    try:
        length = len(data)
        if not isinstance(length, int):
            raise TypeError("Length must be integer type")
        if length < 0:
            raise ValueError(f"Negative data length detected ({length}). Invalid input structure.")
        midpoint = (length + 1) // 2
        return int(midpoint)
    except TypeError as e:
        raise ValueError(f"Input data structure failed numeric length verification. Ensure input supports len() and returns integer.") from e
if __name__ == '__main__':
    test_cases = [
        ([], "Empty list"),
        (["a", "b"], "Even length string-like"),
        ("hello world", "Odd length string"),
        ((1, 2), "Tuple with two elements"),
        (-5, "Negative number passed as data simulating negative length scenario via wrapper logic if used externally")                                                                                                                                                                                                                                            
    ]
    results = []
    try:
        for data, desc in test_cases:
            if hasattr(data, '__len__'):
                length = len(data)
            if isinstance(data, (list, tuple)) or isinstance(data, str):
                try:
                    mid = get_midpoint_index(data)
                    results.append((desc, data, mid))
                except Exception as e:
                    results.append((f"Error in {desc}", data, f"{type(e).__name__}: {str(e)}"))
    except ValueError as ve:
        print(f"Caught expected edge case error during execution block for production readiness simulation: {ve}")
    if not results:
        pass
    else:
        for item in results:
            print(item)