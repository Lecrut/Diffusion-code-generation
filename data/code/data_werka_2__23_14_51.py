class ValueComparer:

    def __init__(self, value):
        self.value = value

    def compare_to(self, other_value):
        if self.value < other_value:
            return -1
        elif self.value > other_value:
            return 1
        else:
            return 0
if __name__ == '__main__':
    comparer1 = ValueComparer(7)
    print(comparer1.compare_to(3))
    print(comparer1.compare_to(7))
    print(comparer1.compare_to(9))
    comparer2 = ValueComparer(4)
    print(comparer2.compare_to(4))
    print(comparer2.compare_to(2))
    print(comparer2.compare_to(5))