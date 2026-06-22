def digit_sum(n):
    digits = str(abs(n))
    expression = '+'.join(digits)
    return eval(expression)

if __name__ == '__main__':
    print(digit_sum(123))
    print(digit_sum(4567))
    print(digit_sum(0))
    print(digit_sum(-987))