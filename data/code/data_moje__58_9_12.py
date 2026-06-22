def count_even_numbers(start, end):
    if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
        raise TypeError("Start and end must be numeric")
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    start_int = int(start)
    end_int = int(end)
    
    if start_int > end_int:
        return 0
    
    if start_int % 2 != 0:
        first_even = start_int + 1
    else:
        first_even = start_int
    
    if end_int % 2 != 0:
        last_even = end_int - 1
    else:
        last_even = end_int
    
    if first_even > last_even:
        return 0
    
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 8))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(1, 1))
    print(count_even_numbers(10, 20))