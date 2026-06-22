class ListComparator:
    _VALID_OPS = ('<', '>', '=')

    @staticmethod
    def _validate_indices(list1, list2, index):
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("Index must be an integer")
        if index < 0:
            raise ValueError("Index cannot be negative")
        if index >= len(list1):
            raise ValueError(f"Index {index} exceeds length of first list")
        if index >= len(list2):
            raise ValueError(f"Index {index} exceeds length of second list")

    @staticmethod
    def _determine_operator(val1, val2):
        if val1 < val2:
            return '<'
        if val1 > val2:
            return '>'
        return '='

    def compare_at_index(self, list1, list2, index):
        self._validate_indices(list1, list2, index)
        val1 = list1[index]
        val2 = list2[index]
        op = self._determine_operator(val1, val2)
        return {
            'left_value': val1,
            'right_value': val2,
            'relation': op
        }

if __name__ == '__main__':
    comparator = ListComparator()
    sample_list_a = [10, 20, 30]
    sample_list_b = [10, 15, 40]
    result = comparator.compare_at_index(sample_list_a, sample_list_b, 1)
    print(result)