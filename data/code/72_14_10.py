class ArrayComparator:
    MATCH = 0
    MISMATCH = 1
    OUT_OF_BOUNDS = 2

    @staticmethod
    def _validate_index(index, length):
        if index < 0 or index >= length:
            return ArrayComparator.OUT_OF_BOUNDS
        return ArrayComparator.MATCH

    @classmethod
    def count_matching_positions(cls, array_a, array_b, positions):
        count = 0
        len_a = len(array_a)
        len_b = len(array_b)
        for pos in positions:
            status_a = cls._validate_index(pos, len_a)
            status_b = cls._validate_index(pos, len_b)
            if status_a == cls.MATCH and status_b == cls.MATCH:
                if array_a[pos] == array_b[pos]:
                    count += 1
        return count

if __name__ == '__main__':
    data_source_1 = [5, 10, 15, 20, 25]
    data_source_2 = [5, 12, 15, 22, 25]
    check_indices = [0, 2, 4]
    comparator = ArrayComparator()
    result = comparator.count_matching_positions(data_source_1, data_source_2, check_indices)
    print(result)