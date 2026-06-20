class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if not (isinstance(list1, list) and isinstance(list2, list)):
            raise ValueError("Both inputs must be lists.")
        if not (0 <= index < len(list1) and 0 <= index < len(list2)):
            raise IndexError("Index out of bounds for the provided lists.")
        
        element1 = list1[index]
        element2 = list2[index]
        
        if element1 == element2:
            return {'list1': element1, 'list2': element2, 'operator': '='}
        elif element1 < element2:
            return {'list1': element1, 'list2': element2, 'operator': '<'}
        else:
            return {'list1': element1, 'list2': element2, 'operator': '>'}

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([5, 10, 15], [3, 8, 15], 2)
    print(result)