def find_final_item_index(item_indices):
    try:
        if not item_indices:
            raise IndexError("Input list of indices cannot be empty")
        return item_indices[-1]
    except TypeError as e:
        raise ValueError("Invalid input type: Expected a list") from e

if __name__ == '__main__':
    test_cases = [
        [1, 5, 2, 8, 3],
        [100],
        [],
        [42],
        [7, 8, 9, 10]
    ]
    
    for i, test_case in enumerate(test_cases):
        try:
            result = find_final_item_index(test_case)
            print(f"Test case {i+1}: {result}")
        except Exception as e:
            print(f"Test case {i+1} raised an exception: {e}")