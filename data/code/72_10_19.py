class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list) or len(data) < max(index1, index2) + 1:
            raise ValueError('Invalid input data')
        return data[index1] == data[index2]
if __name__ == '__main__':
    comparer = ElementComparer()
    result = comparer.compare_at_spots([1, 2, 3, 4, 5], 2, 4)
    print(result)