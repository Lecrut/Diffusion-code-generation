def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55]
    max_value = find_maximum(sample_data)
    print(max_value)