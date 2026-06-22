class ListComparator:
    def __init__(self):
        self._operators = {
            -1: '<',
            0: '=',
            1: '>'
        }

    def _get_operator(self, val1, val2):
        if val1 < val2:
            return self._operators[-1]
        if val1 > val2:
            return self._operators[1]
        return self._operators[0]

    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index >= len(list1):
            raise ValueError("Index out of range for list1")
        if index >= len(list2):
            raise ValueError("Index out of range for list2")
        
        element1 = list1[index]
        element2 = list2[index]
        operator = self._get_operator(element1, element2)
        
        return {
            'element1': element1,
            'element2': element2,
            'operator': operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30]
    list_b = [10, 15, 35]
    
    result1 = comparator.compare_at_index(list_a, list_b, 0)
    print(result1)
    
    result2 = comparator.compare_at_index(list_a, list_b, 1)
    print(result2)
    
    result3 = comparator.compare_at_index(list_a, list_b, 2)
    print(result3)