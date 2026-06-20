class EqualityChecker:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_values_equal(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    checker = EqualityChecker(10, 10)
    print(f"Are values equal? {checker.are_values_equal()}")

    checker = EqualityChecker('hello', 'world')
    print(f"Are values equal? {checker.are_values_equal()}")