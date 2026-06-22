def compare_two_simple_quantities_now_rank_samples(sample1, sample2):
    if not isinstance(sample1, (int, float)) or not isinstance(sample2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    samples = [sample1, sample2]
    ranked_samples = sorted(samples)
    return ranked_samples

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_rank_samples(5.5, 3.14)
    print(result)
    
    result2 = compare_two_simple_quantities_now_rank_samples(7, 7)
    print(result2)
    
    result3 = compare_two_simple_quantities_now_rank_samples(-2, -8)
    print(result3)