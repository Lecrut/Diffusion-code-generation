class ListComparator:
    @staticmethod
    def compare_at_index(list1, list2, index):
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise ValueError("Both inputs must be lists.")
        if not (isinstance(index, int) and 0 <= index < len(list1) and 0 <= index < len(list2)):
            raise ValueError("Index must be a valid integer within the bounds of both lists.")

        value1 = list1[index]
        value2 = list2[index]

        if value1 == value2:
            return {'list1': value1, 'list2': value2, 'operator': '='}
        elif value1 < value2:
            return {'list1': value1, 'list2': value2, 'operator': '<'}
        else:
            return {'list1': value1, 'list2': value2, 'operator': '>'}

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30, 40], [5, 15, 30, 50], 2)
    print(result)