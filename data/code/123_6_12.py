def sum_of_digits(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == '__main__':
    sample_value = -12345
    result = sum_of_digits(sample_value)
    print(result)