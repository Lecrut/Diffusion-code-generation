DIVISOR_BASE = 10

def sum_of_digits(number: int) -> int:
    if number < 0:
        raise ValueError("Input must be a positive integer")
    
    current_sum = 0
    while number > 0:
        digit = number % DIVISOR_BASE
        current_sum += digit
        number //= DIVISOR_BASE
    
    return current_sum

def calculate_and_print_sample(value: int) -> None:
    result = sum_of_digits(value)
    print(result)

if __name__ == '__main__':
    SAMPLE_1 = 56789
    SAMPLE_2 = 42
    SAMPLE_3 = 999999999
    
    calculate_and_print_sample(SAMPLE_1)
    calculate_and_print_sample(SAMPLE_2)
    calculate_and_print_sample(SAMPLE_3)