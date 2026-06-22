class IndexComparator:
    LOWER_THRESHOLD = 0

    @staticmethod
    def validate_index(index, length1, length2):
        if index < IndexComparator.LOWER_THRESHOLD:
            raise ValueError("Index cannot be negative")
        if index >= length1:
            raise ValueError("Index out of bounds for first list")
        if index >= length2:
            raise ValueError("Index out of bounds for second list")

    @classmethod
    def check_less_or_equal(cls, list_one, list_two, index):
        cls.validate_index(index, len(list_one), len(list_two))
        return list_one[index] <= list_two[index]

if __name__ == '__main__':
    values_a = [1, 2, 3]
    values_b = [1, 2, 4]
    target_idx = 2
    result = IndexComparator.check_less_or_equal(values_a, values_b, target_idx)
    print(result)