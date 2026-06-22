def evaluate_conditions(a: int, b: int, c: int) -> bool:
    is_a_positive = a > 0
    is_b_positive = b > 0
    is_c_positive = c > 0
    
    positive_count = int(is_a_positive) + int(is_b_positive) + int(is_c_positive)
    
    return positive_count >= 2

if __name__ == '__main__':
    sample_a = 10
    sample_b = -5
    sample_c = 20
    result = evaluate_conditions(sample_a, sample_b, sample_c)
    print(result)