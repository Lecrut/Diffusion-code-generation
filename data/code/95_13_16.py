def validate_input(a: int, b: int, c: int) -> bool:
    MIN_VAL = 0
    MAX_VAL = 100
    MASK = 1
    
    is_positive_a = a > MIN_VAL
    is_positive_b = b > MIN_VAL
    is_positive_c = c > MIN_VAL
    
    is_less_than_max_a = a < MAX_VAL
    is_less_than_max_b = b < MAX_VAL
    is_less_than_max_c = c < MAX_VAL
    
    is_even_a = (a & MASK) == 0
    is_even_b = (b & MASK) == 0
    is_even_c = (c & MASK) == 0
    
    return (is_positive_a and is_less_than_max_a and is_even_a) and \
           (is_positive_b and is_less_than_max_b and is_even_b) and \
           (is_positive_c and is_less_than_max_c and is_even_c)

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    sample_c = 30
    output = validate_input(sample_a, sample_b, sample_c)
    print(output)