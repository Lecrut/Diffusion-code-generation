def count_even_between(low, high):
    if low > high:
        low, high = high, low
    
    adjusted_low = low if low % 2 == 0 else low + 1
    adjusted_high = high if high % 2 == 0 else high - 1
    
    if adjusted_low > adjusted_high:
        return 0
    
    return (adjusted_high - adjusted_low) // 2 + 1

if __name__ == '__main__':
    result = count_even_between(1, 10)
    print(result)