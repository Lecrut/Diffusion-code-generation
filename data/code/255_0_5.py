def find_max_element(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    for number in numbers[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    sample_data = [4, 2, 9, 6, 3, 7]
    result = find_max_element(sample_data)
    print(result)