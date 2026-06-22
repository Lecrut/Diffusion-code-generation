def count_digits(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    count = 0
    abs_number = abs(number)
    
    while abs_number >= 1:
        abs_number /= 10
        count += 1
    
    return count

if __name__ == '__main__':
    sample_value = -123456
    digit_count = count_digits(sample_value)
    print(digit_count)