class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range for one or both lists")
        
        val1 = list1[index]
        val2 = list2[index]
        
        if val1 < val2:
            operator = '<'
        elif val1 > val2:
            operator = '>'
        else:
            operator = '='
            
        return {
            'element1': val1,
            'element2': val2,
            'comparison': operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [10, 15, 30], 1)
    print(result)