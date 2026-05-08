class ValueChecker:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    a = 10
    b = 10
    c = 5
    d = 8.5
    e = "hello"
    print(f"Is {a} equal to {b}? {checker.check_equality(a, b)}")
    print(f"Is {a} equal to {c}? {checker.check_equality(a, c)}")
    print(f"Is {d} equal to {e}? {checker.check_equality(d, e)}")
    print(f"Is {b} equal to {d}? {checker.check_equality(b, d)}")