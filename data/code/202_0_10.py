def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

if __name__ == '__main__':
    sample_data = [12, 7, 25, 3, 18]
    result = find_max(sample_data)
    print(result)