class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise TypeError("Input 'data' must be a list.")
        if not isinstance(index1, int) or not isinstance(index2, int):
            raise TypeError("Indices 'index1' and 'index2' must be integers.")
        if index1 < 0 or index1 >= len(data) or index2 < 0 or index2 >= len(data):
            raise IndexError("One or both indices are out of bounds for the list.")
        element1 = data[index1]
        element2 = data[index2]
        if element1 == element2:
            return True
        else:
            return False
if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, "apple", [2, 3], {"a": 1}, 4.5]
    print("--- Test Case 1: Equal elements ---")
    result1 = comparer.compare_at_spots(sample_data, 0, 0)
    print(f"Comparing data[0] and data[0]: {result1}")
    print("\n--- Test Case 2: Unequal elements (different types) ---")
    result2 = comparer.compare_at_spots(sample_data, 1, 4)
    print(f"Comparing data[1] ('apple') and data[4] (4.5): {result2}")
    print("\n--- Test Case 3: Unequal elements (different values) ---")
    result3 = comparer.compare_at_spots(sample_data, 0, 1)
    print(f"Comparing data[0] (1) and data[1] ('apple'): {result3}")
    print("\n--- Test Case 4: Comparing identical elements ---")
    result4 = comparer.compare_at_spots(sample_data, 0, 0)
    print(f"Comparing data[0] and data[0]: {result4}")
    print("\n--- Test Case 5: Error Handling (Index Out of Bounds) ---")
    try:
        comparer.compare_at_spots(sample_data, 0, 100)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    print("\n--- Test Case 6: Error Handling (Wrong Type for Data) ---")
    try:
        comparer.compare_at_spots("not a list", 0, 1)
    except TypeError as e:
        print(f"Caught expected error: {e}")
    print("\n--- Test Case 7: Comparing nested structures (Deep comparison is element-wise) ---")
    nested_data = [1, [2, 3], 4]
    result7 = comparer.compare_at_spots(nested_data, 1, 1)
    print(f"Comparing nested_data[1] and nested_data[1]: {result7}")
    result8 = comparer.compare_at_spots(nested_data, 0, 2)
    print(f"Comparing nested_data[0] (1) and nested_data[2] (4): {result8}")