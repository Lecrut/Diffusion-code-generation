class LengthComparator:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def check_equality(self, epsilon=1e-9):
        return abs(self.length1 - self.length2) < epsilon

    def get_absolute_difference(self):
        return abs(self.length1 - self.length2)

if __name__ == '__main__':
    comparator = LengthComparator(3.14159265358979, 3.141592653589793)
    print(comparator.check_equality())
    print(comparator.get_absolute_difference())