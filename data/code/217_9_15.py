import operator

class NumberComparator:
    COMPARATORS = {
        'greater_than': operator.gt,
        'less_than': operator.lt,
        'equal_to': operator.eq
    }
    
    @staticmethod
    def compare_numbers(num1, num2, operation):
        return NumberComparator.COMPARATORS[operation](num1, num2)

if __name__ == '__main__':
    comparator = NumberComparator()
    a = 10
    b = 5
    c = 3
    d = 10
    
    print(f"Is {a} strictly greater than {b}? {comparator.compare_numbers(a, b, 'greater_than')}")
    print(f"Is {c} strictly less than {d}? {comparator.compare_numbers(c, d, 'less_than')}")
    print(f"Is {a} equal to {c}? {comparator.compare_numbers(a, c, 'equal_to')}")