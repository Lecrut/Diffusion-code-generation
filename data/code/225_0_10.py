def find_min_max(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    minimum = maximum = numbers[0]
    for num in numbers[1:]:
        if num < minimum:
            minimum = num
        elif num > maximum:
            maximum = num
    return minimum, maximum

if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 76]
    min_val, max_val = find_min_max(sample_numbers)
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {min_val}")
    print(f"The maximum value is: {max_val}")