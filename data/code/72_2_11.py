class ListComparator:

    def compare_at_index(self, list1, list2, index):
        if index < len(list1) and index < len(list2):
            value1 = list1[index]
            value2 = list2[index]
            if value1 == value2:
                return {'list1': value1, 'list2': value2, 'operator': '='}
            elif value1 < value2:
                return {'list1': value1, 'list2': value2, 'operator': '<'}
            else:
                return {'list1': value1, 'list2': value2, 'operator': '>'}
        else:
            raise IndexError('Index out of bounds')
if __name__ == '__main__':
    comparator = ListComparator()
    result1 = comparator.compare_at_index([10, 20, 30], [5, 15, 30], 2)
    print(result1)
    result2 = comparator.compare_at_index([10, 20, 30], [5, 15, 40], 2)
    print(result2)
    result3 = comparator.compare_at_index([10, 20, 30], [5, 15, 25], 2)
    print(result3)