class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise TypeError("Input 'data' must be a list.")
        if not isinstance(index1, int) or not isinstance(index2, int):
            raise TypeError("Indices 'index1' and 'index2' must be integers.")
        if index1 < 0 or index1 >= len(data) or index2 < 0 or index2 >= len(data):
            raise IndexError("One or both indices are out of bounds for the list.")
        if index1 == index2:
            return True
        if data[index1] == data[index2]:
            return True
        else:
            return False
if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, [3, 4], 5, {'a': 6}, 7]
    print("--- Test Case 1: Equal elements ---")
    result1 = comparer.compare_at_spots(sample_data, 0, 1)
    print(f"Comparing index 0 ({sample_data[0]}) and index 1 ({sample_data[1]}): {result1}")
    print("\n--- Test Case 2: Unequal elements (simple types) ---")
    result2 = comparer.compare_at_spots(sample_data, 0, 3)
    print(f"Comparing index 0 ({sample_data[0]}) and index 3 ({sample_data[3]}): {result2}")
    print("\n--- Test Case 3: Unequal elements (complex types) ---")
    result3 = comparer.compare_at_spots(sample_data, 2, 4)
    print(f"Comparing index 2 ({sample_data[2]}) and index 4 ({sample_data[4]}): {result3}")
    print("\n--- Test Case 4: Same element ---")
    result4 = comparer.compare_at_spots(sample_data, 0, 0)
    print(f"Comparing index 0 ({sample_data[0]}) and index 0 ({sample_data[0]}): {result4}")
    print("\n--- Test Case 5: Error Handling (Index Out of Bounds) ---")
    try:
        comparer.compare_at_spots(sample_data, 0, 10)
    except IndexError as e:
        print(f"Caught expected error: {e}")
    print("\n--- Test Case 6: Error Handling (Wrong Type) ---")
    try:
        comparer.compare_at_spots("not a list", 0, 1)
    except TypeError as e:
        print(f"Caught expected error: {e}")