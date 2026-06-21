class ZeroChecker:
    def __init__(self, numbers):
        self.numbers = numbers

    def contains_zero(self):
        return 0 in self.numbers

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    checker1 = ZeroChecker(sample_list1)
    print(checker1.contains_zero())

    sample_list2 = [0, -1, -2, -3]
    checker2 = ZeroChecker(sample_list2)
    print(checker2.contains_zero())