def find_min_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    minimum = numbers[0]
    maximum = numbers[0]
    
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [45, 7, 23, 89, 6, 51]
    minimum_val, maximum_val = find_min_max(sample_numbers)
    print(f"Minimum value: {minimum_val}")
    print(f"Maximum value: {maximum_val}")