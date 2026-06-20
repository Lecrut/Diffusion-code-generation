class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if index < len(list1) and index < len(list2):
            element1 = list1[index]
            element2 = list2[index]
            if element1 < element2:
                return {'element1': element1, 'element2': element2, 'operator': '<'}
            elif element1 > element2:
                return {'element1': element1, 'element2': element2, 'operator': '>'}
            else:
                return {'element1': element1, 'element2': element2, 'operator': '='}
        else:
            raise IndexError("Index out of range")

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([1, 2, 3], [4, 5, 6], 1)
    print(result)