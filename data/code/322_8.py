import sys
def divide_large_integers(dividend, divisor):
    return dividend // divisor
if __name__ == '__main__':
    dividend = 12345678901234567890
    divisor = 12345
    result = divide_large_integers(dividend, divisor)
    print(result)