def count_even_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")
    if start > end:
        raise ValueError("start must be less than or equal to end")
    
    if start == end:
        return 1 if start % 2 == 0 else 0
    
    count = (end // 2) - ((start - 1) // 2)
    return count

if __name__ == '__main__':
    print(count_even_numbers(1, 10))
    print(count_even_numbers(2, 8))
    print(count_even_numbers(3, 3))
    print(count_even_numbers(-4, 4))
    print(count_even_numbers(0, 0))