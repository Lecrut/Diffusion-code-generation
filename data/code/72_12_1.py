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
    sample_data = [1, 2, "apple", [3, 4], {"a": 1}, 5]
    print("--- Test Case 1: Equal elements ---")
    result1 = comparer.compare_at_spots(sample_data, 0, 0)
    print(f"Comparing index 0 with index 0: {result1}")
    result2 = comparer.compare_at_spots(sample_data, 1, 1)
    print(f"Comparing index 1 with index 1: {result2}")
    result3 = comparer.compare_at_spots(sample_data, 0, 1)
    print(f"Comparing index 0 ({sample_data[0]}) with index 1 ({sample_data[1]}): {result3}")
    print("\n--- Test Case 2: Unequal elements ---")
    result4 = comparer.compare_at_spots(sample_data, 0, 2)
    print(f"Comparing index 0 ({sample_data[0]}) with index 2 ({sample_data[2]}): {result4}")
    result5 = comparer.compare_at_spots(sample_data, 3, 5)
    print(f"Comparing index 3 ({sample_data[3]}) with index 5 ({sample_data[5]}): {result5}")
    print("\n--- Test Case 3: Deep comparison (comparing complex types) ---")
    complex_data = [1, 2, [3, 4], {"a": 1}, 5]
    result6 = comparer.compare_at_spots(complex_data, 2, 3)
    print(f"Comparing index 2 ({complex_data[2]}) with index 3 ({complex_data[3]}): {result6}")
    print("\n--- Test Case 4: Error Handling ---")
    try:
        comparer.compare_at_spots(sample_data, 0, 10)
    except IndexError as e:
        print(f"Caught expected error for out-of-bounds access: {e}")
    try:
        comparer.compare_at_spots(sample_data, 0, "a")
    except TypeError as e:
        print(f"Caught expected error for wrong type: {e}")