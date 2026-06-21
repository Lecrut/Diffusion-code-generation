def find_largest_element(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

if __name__ == '__main__':
    sample_values = [10, 5, 20, 15, 30]
    result = find_largest_element(sample_values)
    print(result)