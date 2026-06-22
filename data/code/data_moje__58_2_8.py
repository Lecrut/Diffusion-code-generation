def count_even_in_range(start, end):
    start_even = start & ~1
    end_even = end & ~1
    
    if start_even > end_even:
        return 0
    
    first_half = start_even + 1
    second_half = end_even - 1
    
    count = 0
    
    if first_half <= second_half:
        count += (second_half - first_half) // 2 + 1
    
    if start_even == start:
        count += 1
    
    if end_even == end:
        count += 1
        
    return count

if __name__ == '__main__':
    start_val = 10
    end_val = 20
    result = count_even_in_range(start_val, end_val)
    print(result)