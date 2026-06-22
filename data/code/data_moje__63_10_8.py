def reverse_digits(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a positive integer")
    
    reversed_num = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
        
    return reversed_num

if __name__ == '__main__':
    print(reverse_digits(12345))
    print(reverse_digits(987654321))
    print(reverse_digits(100))