def find_second_extremes(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")
    
    min1 = max1 = second_min = second_max = float('inf')
    has_duplicate_min = has_duplicate_max = False
    
    for num in numbers:
        if num < min1 or (num == min1 and not has_duplicate_min):
            second_min, min1 = min1, num
            has_duplicate_min = num == min1
        elif min1 < num < second_min:
            second_min = num
        
        if num > max1 or (num == max1 and not has_duplicate_max):
            second_max, max1 = max1, num
            has_duplicate_max = num == max1
        elif min1 < num < second_max:
            second_max = num
    
    return second_min if second_min != float('inf') else None, second_max if second_max != float('inf') else None

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 3, 8, 6]
    print(find_second_extremes(sample_numbers))