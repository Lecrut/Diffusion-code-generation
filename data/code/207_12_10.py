def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_largest(sample_numbers))