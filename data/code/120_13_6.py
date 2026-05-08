class ValueChecker:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    a = 10
    b = 10
    c = 20
    d = "hello"
    e = "hello"
    f = 3.14
    g = 3.14
    print(f"Is {a} equal to {b}? {checker.check_equality(a, b)}")
    print(f"Is {a} equal to {c}? {checker.check_equality(a, c)}")
    print(f"Is '{d}' equal to '{e}'? {checker.check_equality(d, e)}")
    print(f"Is {f} equal to {g}? {checker.check_equality(f, g)}")