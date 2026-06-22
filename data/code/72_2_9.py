class ListComparator:
    _COMPARISON_MAP = {
        -1: '<',
        0: '=',
        1: '>'
    }

    def compare_at_index(self, list1, list2, index):
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range for one or both lists")
        
        val1 = list1[index]
        val2 = list2[index]
        
        if val1 < val2:
            diff = -1
        elif val1 > val2:
            diff = 1
        else:
            diff = 0
            
        operator = self._COMPARISON_MAP[diff]
        
        return {
            'element1': val1,
            'element2': val2,
            'operator': operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30]
    list_b = [10, 15, 40]
    result = comparator.compare_at_index(list_a, list_b, 1)
    print(result)