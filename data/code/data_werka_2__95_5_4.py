def analyze_triplet(first, second, third):
    if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
        raise ValueError("All arguments must be integers")
    if first == 0:
        raise ValueError("First argument cannot be zero for divisibility check")
    
    result_positive = first > 0
    result_even = second % 2 == 0
    result_divisible = third % first == 0
    
    return (result_positive, result_even, result_divisible)

if __name__ == '__main__':
    sample_first = 5
    sample_second = 8
    sample_third = 20
    output = analyze_triplet(sample_first, sample_second, sample_third)
    print(output)