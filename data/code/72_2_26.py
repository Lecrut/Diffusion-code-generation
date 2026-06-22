class ListComparator:
    _EQUALITY_SYMBOL = '='
    _LESS_SYMBOL = '<'
    _GREATER_SYMBOL = '>'

    @staticmethod
    def _get_operator(val1, val2):
        if val1 < val2:
            return ListComparator._LESS_SYMBOL
        if val1 > val2:
            return ListComparator._GREATER_SYMBOL
        return ListComparator._EQUALITY_SYMBOL

    def compare_at_index(self, list1, list2, index):
        if index < 0:
            raise ValueError("Index must be non-negative")
        if index >= len(list1):
            raise ValueError("Index out of range for list1")
        if index >= len(list2):
            raise ValueError("Index out of range for list2")
        
        val1 = list1[index]
        val2 = list2[index]
        operator = self._get_operator(val1, val2)
        
        return {
            'element1': val1,
            'element2': val2,
            'operator': operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [10, 15, 30], 1)
    print(result)