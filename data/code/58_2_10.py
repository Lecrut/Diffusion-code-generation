def count_even_bitwise(start: int, end: int) -> int:
    if start > end:
        return 0
    
    total = end - start + 1
    base_count = total >> 1
    
    remainder = total & 1
    if remainder == 0:
        return base_count
    
    if (start & 1) == 0:
        return base_count + 1
    
    return base_count

if __name__ == '__main__':
    low = 1
    high = 10
    result = count_even_bitwise(low, high)
    print(result)
    
    neg_low = -5
    neg_high = 5
    result_neg = count_even_bitwise(neg_low, neg_high)
    print(result_neg)
    
    single = 4
    result_single = count_even_bitwise(single, single)
    print(result_single)
    
    odd_range = 3
    odd_range_end = 6
    result_odd = count_even_bitwise(odd_range, odd_range_end)
    print(result_odd)