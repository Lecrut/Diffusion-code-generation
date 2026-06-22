def sum_digits(number):
    num_str = str(abs(number))
    digits = num_str.split()
    expression = '+'.join(digits)
    return eval(expression) if digits else 0

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(-678))
    print(sum_digits(0))