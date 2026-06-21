def find_largest_element(numbers):
    if not numbers:
        raise ValueError("The list cannot be empty")
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest

if __name__ == '__main__':
    sample_list = [3.5, 7.2, 1.8, 9.4, 5.6]
    largest_number = find_largest_element(sample_list)
    print(largest_number)