def reverse_integer(n: int) -> int:
    negative = n < 0
    if negative:
        n = -n
    
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    if negative:
        return -reversed_num
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(1200))