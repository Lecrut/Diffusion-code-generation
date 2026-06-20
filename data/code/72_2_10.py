class ListComparator:

    def compare_at_index(self, list1, list2, index):
        if index < len(list1) and index < len(list2):
            value1 = list1[index]
            value2 = list2[index]
            if value1 < value2:
                return {'list1': value1, 'list2': value2, 'operator': '<'}
            elif value1 > value2:
                return {'list1': value1, 'list2': value2, 'operator': '>'}
            else:
                return {'list1': value1, 'list2': value2, 'operator': '='}
        else:
            raise IndexError('Index out of range')
if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([1, 2, 3], [4, 5, 6], 1)
    print(result)