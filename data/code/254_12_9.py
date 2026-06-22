def find_min_element(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = min(numbers)
    return minimum

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 56, 90]
    print(find_min_element(sample_numbers))