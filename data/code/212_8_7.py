def find_second_extremes(numbers):
    if len(numbers) < 2:
        return None, None
    
    min1, min2 = float('inf'), float('inf')
    max1, max2 = float('-inf'), float('-inf')
    
    for num in numbers:
        if num < min1:
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min2 = num
        
        if num > max1:
            max2 = max1
            max1 = num
        elif max1 > num > max2:
            max2 = num
    
    return (min2 if min2 != float('inf') else None, 
            max2 if max2 != float('-inf') else None)

if __name__ == '__main__':
    sample_numbers = [4, 5, 6, 7, 0, 1, 2]
    print(find_second_extremes(sample_numbers))