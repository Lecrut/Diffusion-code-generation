def find_second_extremes(numbers):
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    first_min = second_min = float('inf')
    first_max = second_max = float('-inf')
    
    for num in numbers:
        if num < first_min:
            second_min, first_min = first_min, num
        elif first_min < num < second_min:
            second_min = num
        
        if num > first_max:
            second_max, first_max = first_max, num
        elif first_max > num > second_max:
            second_max = num
    
    return (second_min, second_max)

if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_second_extremes(sample_numbers))