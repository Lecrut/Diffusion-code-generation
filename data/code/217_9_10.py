import operator

def compare_numbers(num1, num2):
    gt = operator.gt(num1, num2)
    lt = operator.lt(num1, num2)
    eq = operator.eq(num1, num2)
    return f"Is {num1} greater than {num2}? {gt}\nIs {num1} less than {num2}? {lt}\nIs {num1} equal to {num2}? {eq}"

if __name__ == '__main__':
    a = 10
    b = 5
    c = 3
    d = 10
    print(compare_numbers(a, b))
    print(compare_numbers(c, d))
    print(compare_numbers(d, a))