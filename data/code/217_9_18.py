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
    print(f"Is {a} strictly greater than {b}? {compare_numbers(a, b)[0]}")
    print(f"Is {c} strictly greater than {d}? {compare_numbers(c, d)[0]}")
    print(f"Is {a} strictly greater than {c}? {compare_numbers(a, c)[0]}")
    print(f"Is {b} strictly greater than {a}? {compare_numbers(b, a)[0]}")