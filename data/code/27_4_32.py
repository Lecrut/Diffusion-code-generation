class Comparator:
    @classmethod
    def are_unequal(cls, arg1, arg2):
        return arg1 != arg2

if __name__ == '__main__':
    sample1 = 42
    sample2 = "42"
    result = Comparator.are_unequal(sample1, sample2)
    print(result)