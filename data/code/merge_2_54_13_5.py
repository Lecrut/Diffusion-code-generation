import sys
def find_midpoint_index(data):
    try:
        if not hasattr(data, '__len__') or isinstance(data, (str, bytes)):
            raise TypeError("Input must be a list-like object excluding strings and bytes.")
        length = len(data)
        if length < 0:
            return None
        mid_index = length // 2
        return int(mid_index)
    except TypeError as e:
        raise ValueError(f"Invalid input structure or non-numeric context detected. Error: {e}")
if __name__ == '__main__':
    test_cases = [
        ["a", "b", "c"],                                             
        [1, 2],                                                                 
        [],                                                                                                                 
        [-1],                                                                       
    ]
    results = []
    for idx, data in enumerate(test_cases):
        try:
            mid_idx = find_midpoint_index(data)
            if mid_idx is None or isinstance(mid_idx, int):
                results.append(f"Test {idx}: Input={data}, Midpoint Index={mid_idx}")
            else:
                print("Unexpected return type in test case")
        except Exception as e:
            results.append(f"Test {idx}: Input={data}, Error occurred (Expected behavior): {e}")
    print("Execution Results:")
    for res in results:
        print(res)