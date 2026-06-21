class IndexComparator:
    MIN_INDEX = 0

    @staticmethod
    def validate_bounds(index, length):
        if index < IndexComparator.MIN_INDEX:
            raise ValueError("Index cannot be negative")
        if index >= length:
            raise ValueError("Index out of range")

    @staticmethod
    def compare(list_first, list_second, index):
        IndexComparator.validate_bounds(index, len(list_first))
        IndexComparator.validate_bounds(index, len(list_second))
        val_one = list_first[index]
        val_two = list_second[index]
        return val_one <= val_two

if __name__ == '__main__':
    data_a = [1, 3, 5]
    data_b = [2, 2, 6]
    target = 1
    outcome = IndexComparator.compare(data_a, data_b, target)
    print(outcome)