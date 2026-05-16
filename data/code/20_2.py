class Comparator:
    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    c = Comparator()
    print(c.check_equality(10, 10))
    print(c.check_equality("hello", "hello"))
    print(c.check_equality(5, 6))
    print(c.check_equality([1, 2], [1, 2]))
    print(c.check_equality(3.14, 3.1400000000000004))