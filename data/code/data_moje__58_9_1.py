def count_even_numbers(start: int, stop: int) -> int:
    if start > stop:
        start, stop = stop, start
    
    first_even = start if start % 2 == 0 else start + 1
    if first_even > stop:
        return 0
    
    return (stop - first_even) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)
    result = count_even_numbers(10, 20)
    print(result)
    result = count_even_numbers(-5, 5)
    print(result)
    result = count_even_numbers(2, 2)
    print(result)
    result = count_even_numbers(3, 3)
    print(result)