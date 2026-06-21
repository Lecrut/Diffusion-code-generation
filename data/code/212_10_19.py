def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    minimum = numbers[0]
    maximum = numbers[0]
    
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    min_val, max_val = find_min_max(sample_list)
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")