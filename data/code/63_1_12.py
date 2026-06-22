def reverse_integer(n: int) -> int:
    reversed_num = 0
    sign = -1 if n < 0 else 1
    n_abs = abs(n)
    
    while n_abs > 0:
        reversed_num = reversed_num * 10 + n_abs % 10
        n_abs //= 10
    
    return reversed_num * sign

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-67890))
    print(reverse_integer(100))