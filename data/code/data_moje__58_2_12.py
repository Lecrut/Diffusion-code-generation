def count_even_in_range(start, end):
    if start > end:
        start, end = end, start
    
    count = 0
    current = start
    
    while current <= end:
        if (current & 1) == 0:
            count += 1
        current += 1
    
    return count

if __name__ == '__main__':
    start_val = 1
    end_val = 10
    result = count_even_in_range(start_val, end_val)
    print(result)