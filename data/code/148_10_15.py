def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [3, 7, 2, 5, 9, 1]
    largest = find_largest(sample_list)
    print(largest)