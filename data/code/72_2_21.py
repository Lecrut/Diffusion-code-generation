class ListComparator:
    _VALID_OPS = ('<', '>', '=')

    @staticmethod
    def _determine_operator(val1, val2):
        if val1 < val2:
            return '<'
        if val1 > val2:
            return '>'
        return '='

    def compare_at_index(self, list1, list2, index):
        len1 = len(list1)
        len2 = len(list2)
        if index < 0 or index >= len1 or index >= len2:
            raise ValueError("Index out of range")
        val1 = list1[index]
        val2 = list2[index]
        op = self._determine_operator(val1, val2)
        return {
            'element1': val1,
            'element2': val2,
            'operator': op
        }

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30]
    list_b = [10, 15, 35]
    result = comparator.compare_at_index(list_a, list_b, 1)
    print(result)