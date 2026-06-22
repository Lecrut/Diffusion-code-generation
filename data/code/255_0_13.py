def find_max_element(numbers):
    if not numbers:
        return None
    max_element = numbers[0]
    for number in numbers[1:]:
        if number > max_element:
            max_element = number
    return max_element
if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5, 6, 8, 4, 1]
    result = find_max_element(sample_values)
    print(result)