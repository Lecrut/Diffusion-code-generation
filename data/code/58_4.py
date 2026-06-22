def count_even_numbers(low: int, high: int) -> int:
    if low > high:
        low, high = high, low
    
    start = low if low % 2 == 0 else low + 1
    end = high if high % 2 == 0 else high - 1
    
    if start > end:
        return 0
    
    return (end - start) // 2 + 1

if __name__ == '__main__':
    result = count_even_numbers(1, 10)
    print(result)