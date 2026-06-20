def sum_of_digits(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    digit_sum = 0
    for digit in str(n):
        digit_sum += int(digit)
    
    return digit_sum

if __name__ == '__main__':
    print(sum_of_digits(12345))
    print(sum_of_digits(0))
    print(sum_of_digits(9876))