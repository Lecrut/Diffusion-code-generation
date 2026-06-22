def compare_two_simple_quantities_now_rank_samples(a, b):
    return sorted([a, b])

if __name__ == '__main__':
    sample1 = 10.5
    sample2 = 5.2
    print(compare_two_simple_quantities_now_rank_samples(sample1, sample2))
    
    sample3 = 3
    sample4 = 7
    print(compare_two_simple_quantities_now_rank_samples(sample3, sample4))
    
    sample5 = -1.0
    sample6 = -5.0
    print(compare_two_simple_quantities_now_rank_samples(sample5, sample6))