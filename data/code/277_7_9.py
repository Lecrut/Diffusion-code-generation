def count_digits(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    count = 0
    abs_number = abs(number)
    
    while abs_number > 0:
        count += 1
        abs_number //= 10
    
    return count

if __name__ == '__main__':
    sample_value = -123456789
    result = count_digits(sample_value)
    print(result)