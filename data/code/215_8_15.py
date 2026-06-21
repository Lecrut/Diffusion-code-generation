def determine_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

if __name__ == '__main__':
    sample_a = 15
    sample_b = 25
    sample_c = 35
    
    result = determine_largest(sample_a, sample_b, sample_c)
    print(f"The largest number among {sample_a}, {sample_b}, and {sample_c} is: {result}")