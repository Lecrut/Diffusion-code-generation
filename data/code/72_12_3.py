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
        return data[index1] == data[index2]
if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, "apple", [3, 4], {"a": 1}, 5]
    try:
        result1 = comparer.compare_at_spots(sample_data, 0, 1)
        print(f"Comparing data[0] ({sample_data[0]}) and data[1] ({sample_data[1]}): {result1}")
        result2 = comparer.compare_at_spots(sample_data, 2, 5)
        print(f"Comparing data[2] ({sample_data[2]}) and data[5] ({sample_data[5]}): {result2}")
        result3 = comparer.compare_at_spots(sample_data, 3, 3)
        print(f"Comparing data[3] ({sample_data[3]}) and data[3] ({sample_data[3]}): {result3}")
        result4 = comparer.compare_at_spots(sample_data, 0, 0)
        print(f"Comparing data[0] ({sample_data[0]}) and data[0] ({sample_data[0]}): {result4}")
        print("\nTesting error handling:")
        try:
            comparer.compare_at_spots(sample_data, 0, 10)
        except IndexError as e:
            print(f"Caught expected error: {e}")
        try:
            comparer.compare_at_spots([1, 2], 0, -1)
        except IndexError as e:
            print(f"Caught expected error: {e}")
        try:
            comparer.compare_at_spots("not a list", 0, 1)
        except TypeError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")