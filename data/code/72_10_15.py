class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list) or len(data) < 2:
            raise ValueError('Input must be a non-empty list')
        if not 0 <= index1 < len(data) or not 0 <= index2 < len(data):
            raise IndexError('Indices out of range')
        return data[index1] == data[index2]
if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, 2, 3, 4, 5]
    print(comparer.compare_at_spots(sample_data, 1, 3))
    print(comparer.compare_at_spots(sample_data, 0, 0))