def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    
    minimum = maximum = numbers[0]
    
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [42, 7, 38, 56, 23, 9]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")