class ValueComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_equal(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    comparator1 = ValueComparator(10, 10)
    print(f"Are the values equal? {comparator1.are_equal()}")

    comparator2 = ValueComparator(10, 20)
    print(f"Are the values equal? {comparator2.are_equal()}")