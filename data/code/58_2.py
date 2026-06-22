def count_even(start: int, end: int) -> int:
    if start > end:
        return 0
    abs_start = abs(start)
    abs_end = abs(end)
    
    if start >= 0 and end >= 0:
        count_end = abs_end >> 1
        count_start = (abs_start - 1) >> 1
        return count_end - count_start
    
    if start < 0 and end < 0:
        count_start_neg = (abs_start - 1) >> 1
        count_end_neg = abs_end >> 1
        return count_end_neg - count_start_neg
    
    pos_count = (end - 1) >> 1
    neg_count = (abs_start - 1) >> 1
    if start <= 0:
        neg_count += 1
    if end >= 0:
        pos_count += 1
    return neg_count + pos_count

if __name__ == '__main__':
    result = count_even(-10, 10)
    print(result)
    
    result2 = count_even(1, 10)
    print(result2)
    
    result3 = count_even(2, 10)
    print(result3)