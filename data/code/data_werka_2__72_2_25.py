class ListComparator:
    _RESULT_KEYS = ('element1', 'element2', 'operator')

    @staticmethod
    def _determine_operator(val1, val2):
        if val1 < val2:
            return '<'
        if val1 > val2:
            return '>'
        return '='

    def compare_at_index(self, list1, list2, index):
        if not isinstance(index, int):
            raise ValueError("Index must be an integer")
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError("Index out of range for one or both lists")
        
        element1 = list1[index]
        element2 = list2[index]
        operator = self._determine_operator(element1, element2)
        
        return {
            'element1': element1,
            'element2': element2,
            'operator': operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    result = comparator.compare_at_index([10, 20, 30], [10, 15, 30], 1)
    print(result)