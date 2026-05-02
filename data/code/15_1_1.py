class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Are 10 and 10 equal? {checker.are_equal(10, 10)}")
    print(f"Are 'hello' and 'hello' equal? {checker.are_equal('hello', 'hello')}")
    print(f"Are 5 and 6 equal? {checker.are_equal(5, 6)}")
    print(f"Are True and True equal? {checker.are_equal(True, True)}")
    print(f"Are 3.14 and 3.1400000000000001 equal? {checker.are_equal(3.14, 3.1400000000000001)}")
    print(f"Are [1, 2] and [1, 2] equal? {checker.are_equal([1, 2], [1, 2])}")
    print(f"Are {'a'} and 'b' equal? {checker.are_equal('a', 'b')}")