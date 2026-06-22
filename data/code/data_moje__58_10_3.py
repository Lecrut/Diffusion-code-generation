def count_even_numbers_in_range(start: int, end: int) -> int:
    if start > end:
        return 0
    if start % 2 == 0:
        start_count = 0
    else:
        start_count = 1
    
    if end % 2 == 0:
        end_count = 0
    else:
        end_count = 1
    
    total_count = end - start + 1
    if total_count % 2 == 0:
        return total_count // 2
    else:
        if start_count == end_count:
            return total_count // 2 + start_count
        else:
            return total_count // 2

if __name__ == '__main__':
    result = count_even_numbers_in_range(2, 10)
    print(result)