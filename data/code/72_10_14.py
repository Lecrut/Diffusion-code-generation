class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list) or len(data) < max(index1, index2) + 1:
            raise ValueError("Invalid input: 'data' must be a non-empty list with indices within its bounds.")
        return data[index1] == data[index2]
if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [10, 'hello', [3, 4], {'a': 5}]
    result = comparer.compare_at_spots(sample_data, 1, 2)
    print(result)