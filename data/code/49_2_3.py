class LengthComparator:
    def __init__(self, length1, length2, comparator_func):
        self.length1 = length1
        self.length2 = length2
        self.comparator_func = comparator_func
    def compare_and_print(self):
        result = self.comparator_func(self.length1, self.length2)
        print(f"Length 1: {self.length1}")
        print(f"Length 2: {self.length2}")
        print(f"Comparison Result: {result}")
if __name__ == '__main__':
    def compare_lengths(a, b):
        if a > b:
            return "Length 1 is greater than Length 2"
        elif a < b:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"
    len_a = 15
    len_b = 25
    comparator = LengthComparator(len_a, len_b, compare_lengths)
    comparator.compare_and_print()
    len_c = 100
    len_d = 100
    comparator_2 = LengthComparator(len_c, len_d, compare_lengths)
    comparator_2.compare_and_print()
    len_e = 5
    len_f = 8
    comparator_3 = LengthComparator(len_e, len_f, compare_lengths)
    comparator_3.compare_and_print()