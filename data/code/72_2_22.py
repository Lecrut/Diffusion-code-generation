class ListComparator:
    _VALID_OPERATORS = ('<', '>', '=')
    _ERROR_MSG = "Index out of range for one or both lists"

    def compare_at_index(self, list1, list2, index):
        if index < 0 or index >= len(list1) or index >= len(list2):
            raise ValueError(self._ERROR_MSG)
        val1 = list1[index]
        val2 = list2[index]
        if val1 < val2:
            op = self._VALID_OPERATORS[0]
        elif val1 > val2:
            op = self._VALID_OPERATORS[2]
        else:
            op = self._VALID_OPERATORS[1]
        return {
            'element1': val1,
            'element2': val2,
            'operator': op
        }

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30]
    list_b = [10, 15, 35]
    idx = 1
    result = comparator.compare_at_index(list_a, list_b, idx)
    print(result)