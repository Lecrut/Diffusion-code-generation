class ListComparator:

    def compare_at_index(self, list1, list2, index):
        if index < len(list1) and index < len(list2):
            value1 = list1[index]
            value2 = list2[index]
            if value1 == value2:
                return {'value1': value1, 'value2': value2, 'operator': '='}
            elif value1 < value2:
                return {'value1': value1, 'value2': value2, 'operator': '<'}
            else:
                return {'value1': value1, 'value2': value2, 'operator': '>'}
        else:
            return {'error': 'Index out of range'}
if __name__ == '__main__':
    comparator = ListComparator()
    result1 = comparator.compare_at_index([5, 6, 7], [3, 4, 8], 2)
    print(result1)
    result2 = comparator.compare_at_index([1, 2, 3], [4, 5, 6], 1)
    print(result2)
    result3 = comparator.compare_at_index([10, 20], [30, 40, 50], 1)
    print(result3)