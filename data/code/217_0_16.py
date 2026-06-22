class IntegerComparator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def compare(x, y):
        if x > y:
            return "greater than"
        elif x < y:
            return "less than"
        else:
            return "equal to"

    def get_comparison_result(self):
        return IntegerComparator.compare(self.a, self.b)

if __name__ == '__main__':
    comparator = IntegerComparator(10, 5)
    result = comparator.get_comparison_result()
    print(result)