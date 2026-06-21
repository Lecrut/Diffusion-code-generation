def find_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    input_data = [10, 5, 22, 8, 30, 15]
    largest_number = find_max(input_data)
    print(largest_number)