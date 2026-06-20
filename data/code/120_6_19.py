class EqualityTester:
    def are_values_equal(self, a, b):
        return a == b

if __name__ == '__main__':
    tester = EqualityTester()
    print(tester.are_values_equal(10, 10))
    print(tester.are_values_equal(10, 20))
    print(tester.are_values_equal('hello', 'hello'))
    print(tester.are_values_equal('hello', 'world'))