class NumberComparator:
    @staticmethod
    def compare(num1, num2):
        return (num1 > num2, num1 < num2, num1 == num2)

if __name__ == '__main__':
    comparator = NumberComparator()
    a = 10
    b = 5
    c = 3
    d = 10
    results = [
        comparator.compare(a, b),
        comparator.compare(c, d),
        comparator.compare(d, a)
    ]
    print(f"Is {a} greater than {b}? {results[0][0]}")
    print(f"Is {c} greater than {d}? {results[1][0]}")
    print(f"Is {d} greater than {a}? {results[2][0]}")