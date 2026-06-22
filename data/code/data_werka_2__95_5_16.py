def evaluate_integers(first, second, third):
    if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
        raise ValueError("All inputs must be integers")
    
    if first == 0:
        raise ValueError("First integer cannot be zero for divisibility check")
    
    is_first_positive = first > 0
    is_second_even = second % 2 == 0
    is_third_divisible = third % first == 0
    
    return (is_first_positive, is_second_even, is_third_divisible)

if __name__ == '__main__':
    sample_first = 7
    sample_second = 8
    sample_third = 21
    result = evaluate_integers(sample_first, sample_second, sample_third)
    print(result)