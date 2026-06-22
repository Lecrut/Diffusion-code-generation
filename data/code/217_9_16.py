import operator

class NumberComparator:
    def __init__(self):
        self.ops = {
            'greater_than': operator.gt,
            'less_than': operator.lt,
            'equal_to': operator.eq
        }

    def compare(self, num1, num2, operation):
        return self.ops[operation](num1, num2)

if __name__ == '__main__':
    comparator = NumberComparator()
    a = 10
    b = 5
    c = 3
    d = 10

    print(f"Is {a} greater than {b}? {comparator.compare(a, b, 'greater_than')}")
    print(f"Is {c} less than {d}? {comparator.compare(c, d, 'less_than')}")
    print(f"Is {a} equal to {c}? {comparator.compare(a, c, 'equal_to')}")
    print(f"Is {b} greater than {a}? {comparator.compare(b, a, 'greater_than')}")