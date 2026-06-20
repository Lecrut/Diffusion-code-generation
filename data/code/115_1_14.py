def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

if __name__ == '__main__':
    result = divide(100, 3)
    print(result)