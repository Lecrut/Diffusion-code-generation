def find_max_element(numbers):
    if not numbers:
        return None
    max_element = numbers[0]
    for number in numbers[1:]:
        if number > max_element:
            max_element = number
    return max_element
if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max_element(sample_values))