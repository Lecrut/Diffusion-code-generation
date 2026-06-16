def find_maximum(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    sample_data = [3, 5, -2, 9, 7.5, 4]
    result = find_maximum(sample_data)
    print(result)