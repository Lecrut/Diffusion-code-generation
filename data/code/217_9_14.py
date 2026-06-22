import operator

def compare_numbers(num1, num2):
    greater = operator.gt(num1, num2)
    less = operator.lt(num1, num2)
    equal = operator.eq(num1, num2)
    return greater, less, equal

if __name__ == '__main__':
    a = 10
    b = 5
    c = 10
    d = 20
    results = compare_numbers(a, b), compare_numbers(c, d), compare_numbers(a, c), compare_numbers(b, a)
    print(f"Is {a} strictly greater than {b}? {results[0][0]}")
    print(f"Is {c} strictly greater than {d}? {results[1][0]}")
    print(f"Is {a} strictly greater than {c}? {results[2][0]}")
    print(f"Is {b} strictly greater than {a}? {results[3][0]}")