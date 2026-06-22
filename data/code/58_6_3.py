def count_even_numbers(min_val, max_val):
    if min_val > max_val:
        return 0
    
    first_even = min_val + (min_val % 2)
    last_even = max_val - (max_val % 2)
    
    if first_even > last_even:
        return 0
    
    count = (last_even - first_even) // 2 + 1
    return count

if __name__ == '__main__':
    result = count_even_numbers(2, 10)
    print(result)
    
    result2 = count_even_numbers(1, 5)
    print(result2)
    
    result3 = count_even_numbers(10, 10)
    print(result3)
    
    result4 = count_even_numbers(11, 11)
    print(result4)