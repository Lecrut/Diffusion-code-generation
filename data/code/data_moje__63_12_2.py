def reverse_integer(n):
    negative = n < 0
    num_str = str(abs(n))
    reversed_str = num_str[::-1]
    reversed_num = int(reversed_str)
    if negative:
        reversed_num = -reversed_num
    if reversed_num > 2**31 - 1 or reversed_num < -2**31:
        return 0
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(1200))
    print(reverse_integer(1001))
    print(reverse_integer(0))