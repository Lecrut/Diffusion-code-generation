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
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index must be non-negative")
        if index >= len(list1):
            raise ValueError("Index out of range for list1")
        if index >= len(list2):
            raise ValueError("Index out of range for list2")

        element1 = list1[index]
        element2 = list2[index]
        operator = self._determine_operator(element1, element2)

        return {
            self._RESULT_KEYS[0]: element1,
            self._RESULT_KEYS[1]: element2,
            self._RESULT_KEYS[2]: operator
        }

if __name__ == '__main__':
    comparator = ListComparator()
    sample_list_a = [10, 20, 30]
    sample_list_b = [5, 20, 35]
    target_index = 0
    result = comparator.compare_at_index(sample_list_a, sample_list_b, target_index)
    print(result)