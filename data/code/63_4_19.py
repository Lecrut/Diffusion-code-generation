def reverse_integer(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n == 0:
        return 0
    
    negative = n < 0
    if negative:
        n = -n
        
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
        
    if negative:
        return -reversed_num
    return reversed_num

if __name__ == '__main__':
    print(reverse_integer(12345))
    print(reverse_integer(-6789))
    print(reverse_integer(1000))
    print(reverse_integer(0))
    print(reverse_integer(9))