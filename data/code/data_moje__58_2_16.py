def count_even_in_range(start: int, end: int) -> int:
    adjusted_start = start
    adjusted_end = end
    
    if adjusted_start & 1:
        adjusted_start += 1
    if adjusted_end & 1:
        adjusted_end -= 1
        
    if adjusted_start > adjusted_end:
        return 0
        
    count = (adjusted_end - adjusted_start) >> 1
    return count + 1

if __name__ == '__main__':
    start_value = 10
    end_value = 20
    result = count_even_in_range(start_value, end_value)
    print(result)