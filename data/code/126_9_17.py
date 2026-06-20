class ValueComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_equal(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    comparator = ValueComparator(30, 30)
    result = comparator.check_equal()
    print(result)