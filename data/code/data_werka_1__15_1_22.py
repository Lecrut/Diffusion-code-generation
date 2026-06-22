class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()
    result1 = checker.are_equal(42, 42)
    result2 = checker.are_equal('hello', 'world')
    print(f"Are 42 and 42 equal? {result1}")
    print(f"Are 'hello' and 'world' equal? {result2}")