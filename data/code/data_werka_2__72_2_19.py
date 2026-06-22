class ListComparator:
    def compare_at_index(self, list1, list2, index):
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range")
        
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
    list_a = [10, 20, 30]
    list_b = [10, 15, 35]
    result = comparator.compare_at_index(list_a, list_b, 1)
    print(result)