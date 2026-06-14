def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum
if __name__ == '__main__':
    sample_numbers = [15, 3, 88, 42, 9, 76]
    minimum_val, maximum_val = find_min_max(sample_numbers)
    print(f"The list of numbers is: {sample_numbers}")
    print(f"The minimum value is: {minimum_val}")
    print(f"The maximum value is: {maximum_val}")