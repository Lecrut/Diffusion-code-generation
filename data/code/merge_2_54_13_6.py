import sys
def find_midpoint_index(data):
    try:
        length = len(data)
        if length < 0:
            return None
        if length == 0:
            return None
        midpoint = (length - 1) // 2
        return midpoint
    except TypeError as e:
        raise TypeError(f"Input must be a list-like structure, got {type(data).__name__}.") from e
if __name__ == '__main__':
    test_cases = [
        [],                                         
        [-1],                                                                
        [0, 1],                                   
        [0, 1, 2],                               
        ["a", "b"],                                                                                                   
        [10],                                                 
    ]
    for i, test_data in enumerate(test_cases):
        try:
            result = find_midpoint_index(test_data)
            print(f"Test case {i}: Input={test_data}, Midpoint Index={result}")
        except Exception as ex:
            print(f"Test case {i} Error: {ex.__class__.__name__}: {ex}")
    print("Explicit Single Element Test:")
    try:
        res = find_midpoint_index([42])
        assert res == 0, f"Expected 0, got {res}"
        print(f"Single element [42] -> {res} (Correct)")
    except AssertionError as e:
        print(e)
    print("Explicit Empty List Test:")
    try:
        res = find_midpoint_index([])
        assert res is None, f"Expected None, got {res}"
        print(f"Empty list [] -> {res} (Correct)")
    except AssertionError as e:
        print(e)
    print("Explicit Non-List Type Test:")
    try:
        res = find_midpoint_index(12345)                                                                                   
        assert False, "Should have raised TypeError"
    except TypeError as e:
        print(f"Integer input {12345} -> Raised TypeError (Correct): {e}")
    print("All tests completed.")