def count_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    count_up_to_end = end // 2
    count_before_start = (start - 1) // 2
    
    return count_up_to_end - count_before_start

if __name__ == '__main__':
    result1 = count_even_numbers(1, 10)
    print(result1)
    result2 = count_even_numbers(4, 15)
    print(result2)
    result3 = count_even_numbers(2, 2)
    print(result3)
    result4 = count_even_numbers(-5, 5)
    print(result4)