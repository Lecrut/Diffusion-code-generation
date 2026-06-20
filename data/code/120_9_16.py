class EqualityChecker:
    @staticmethod
    def are_equal(a, b):
        if type(a) != type(b):
            return False
        return a == b

if __name__ == '__main__':
    print(f"Test 1 (Integers): {EqualityChecker.are_equal(10, 10)}")
    print(f"Test 2 (Floats): {EqualityChecker.are_equal(3.14, 3.14)}")
    print(f"Test 3 (Strings): {EqualityChecker.are_equal('hello', 'hello')}")
    print(f"Test 4 (Strings unequal): {EqualityChecker.are_equal('hello', 'world')}")
    print(f"Test 5 (Mixed types unequal): {EqualityChecker.are_equal(10, '10')}")
    print(f"Test 6 (Different types unequal): {EqualityChecker.are_equal(10.0, 10)}")