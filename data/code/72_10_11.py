class ElementComparer:
    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        if not all(isinstance(i, int) for i in [index1, index2]):
            raise ValueError("Indices must be integers")
        if index1 < 0 or index1 >= len(data):
            raise IndexError(f"Index {index1} is out of bounds")
        if index2 < 0 or index2 >= len(data):
            raise IndexError(f"Index {index2} is out of bounds")

        return data[index1] == data[index2]

if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [10, 20, 30, 40, 50, 60, 70, 80]
    result = comparer.compare_at_spots(sample_data, 0, 2)
    print(f"Comparing index 0 ({sample_data[0]}) with index 2 ({sample_data[2]}): {result}")