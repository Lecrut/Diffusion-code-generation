class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index must be non-negative")
        if index >= len(list1):
            raise ValueError("Index out of range for list1")
        if index >= len(list2):
            raise ValueError("Index out of range for list2")
        
        element1 = list1[index]
        element2 = list2[index]
        
        if element1 < element2:
            relation = '<'
        elif element1 > element2:
            relation = '>'
        else:
            relation = '='
            
        return {
            'value1': element1,
            'value2': element2,
            'result': relation
        }

if __name__ == '__main__':
    comparator = ListComparator()
    l1 = [10, 20, 30]
    l2 = [10, 25, 30]
    print(comparator.compare_at_index(l1, l2, 1))