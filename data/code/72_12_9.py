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
    sample_data = [1, "apple", [2, 3], {"a": 4}, 5.5]
    try:
        result1 = comparer.compare_at_spots(sample_data, 0, 4)
        print(f"Comparison between index 0 ({sample_data[0]}) and index 4 ({sample_data[4]}): {result1}")
        result2 = comparer.compare_at_spots(sample_data, 1, 2)
        print(f"Comparison between index 1 ({sample_data[1]}) and index 2 ({sample_data[2]}): {result2}")
        result3 = comparer.compare_at_spots(sample_data, 0, 0)
        print(f"Comparison between index 0 ({sample_data[0]}) and index 0 ({sample_data[0]}): {result3}")
        result4 = comparer.compare_at_spots(sample_data, 5, 0)
        print(f"Comparison between index 5 and index 0: {result4}")
        comparer.compare_at_spots(sample_data, 5, 0)
    except (TypeError, IndexError) as e:
        print(f"Error during comparison: {e}")