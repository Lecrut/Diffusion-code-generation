def find_minimum(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    minimum = min(numbers)
    return minimum

if __name__ == '__main__':
    sample_values = [45, 12, 89, 3, 67, 22]
    result = find_minimum(sample_values)
    print(result)