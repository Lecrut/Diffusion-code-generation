def compare_two_simple_quantities_now_rank_samples(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return sorted([a, b])

if __name__ == '__main__':
    sample1 = compare_two_simple_quantities_now_rank_samples(10, 5)
    print(sample1)
    
    sample2 = compare_two_simple_quantities_now_rank_samples(3.14, 3.14)
    print(sample2)
    
    sample3 = compare_two_simple_quantities_now_rank_samples(-1, -5)
    print(sample3)