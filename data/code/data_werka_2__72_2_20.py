class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range")
        
        val1 = list1[index]
        val2 = list2[index]
        
        if val1 < val2:
            op = '<'
        elif val1 > val2:
            op = '>'
        else:
            op = '='
            
        return {
            'element1': val1,
            'element2': val2,
            'operator': op
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [10, 15, 30], 1)
    print(result)
    result2 = comparator.compare_at_index([5, 6], [5, 7], 0)
    print(result2)