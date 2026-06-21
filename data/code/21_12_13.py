class NumberComparator:
    MAX_VALUE_THRESHOLD = 0

    @staticmethod
    def _determine_max(x, y):
        return x if x > y else y

    @classmethod
    def get_highest(cls, first, second, third):
        pair_max = cls._determine_max(first, second)
        return cls._determine_max(pair_max, third)

if __name__ == '__main__':
    val_one = 42
    val_two = 17
    val_three = 99
    computed_result = NumberComparator.get_highest(val_one, val_two, val_three)
    print(computed_result)