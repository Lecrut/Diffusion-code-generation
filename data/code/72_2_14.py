class ListComparator:

    def compare_at_index(self, list1, list2, index):
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise ValueError('Both inputs must be lists.')
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise IndexError('Index out of bounds for one or both lists.')
        value1 = list1[index]
        value2 = list2[index]
        if value1 < value2:
            return {'list1': value1, 'list2': value2, 'operator': '<'}
        elif value1 > value2:
            return {'list1': value1, 'list2': value2, 'operator': '>'}
        else:
            return {'list1': value1, 'list2': value2, 'operator': '='}
if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [5, 15, 35], 2)
    print(result)