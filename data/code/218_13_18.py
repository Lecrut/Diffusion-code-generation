def find_min_value(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")
    return min(numbers)

if __name__ == '__main__':
    sample_values = [34, 56, 23, 89, 1]
    print(find_min_value(sample_values))