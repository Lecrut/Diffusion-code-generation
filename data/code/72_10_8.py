class ElementComparer:

    def compare_at_spots(self, data, index1, index2):
        if not isinstance(data, list) or len(data) < max(index1, index2) + 1:
            raise ValueError('Invalid input: data must be a list with at least index1 and index2 elements')
        try:
            element1 = data[index1]
            element2 = data[index2]
        except IndexError as e:
            raise IndexError(f'Index out of range: {e}')
        if element1 == element2:
            return 'Elements are equal'
        elif element1 < element2:
            return 'Element at index1 is less than element at index2'
        else:
            return 'Element at index1 is greater than element at index2'
if __name__ == '__main__':
    comparer = ElementComparer()
    result = comparer.compare_at_spots([1, 3, 5, 7], 1, 3)
    print(result)