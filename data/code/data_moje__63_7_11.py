def reverse_digits(n: int) -> int:
    negative = n < 0
    num = -n if negative else n
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return -reversed_num if negative else reversed_num

if __name__ == '__main__':
    print(reverse_digits(12345))
    print(reverse_digits(-6789))
    print(reverse_digits(100))
    print(reverse_digits(0))