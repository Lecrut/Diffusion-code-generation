def find_largest_element(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest_element(sample_values))