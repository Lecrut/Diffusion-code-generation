def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    minimum = maximum = numbers[0]
    
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 71]
    minimum_val, maximum_val = find_min_max(sample_numbers)
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")