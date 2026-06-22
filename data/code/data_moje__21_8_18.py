class NumericComparator:
    INPUT_COUNT = 3

    @staticmethod
    def _compare_pair(first, second):
        if first >= second:
            return first
        return second

    @staticmethod
    def find_largest(value_a, value_b, value_c):
        partial_max = NumericComparator._compare_pair(value_a, value_b)
        final_max = NumericComparator._compare_pair(partial_max, value_c)
        return final_max

if __name__ == '__main__':
    sample_x = 15.5
    sample_y = 42.0
    sample_z = 31.2
    comparator = NumericComparator()
    largest_value = comparator.find_largest(sample_x, sample_y, sample_z)
    print(largest_value)