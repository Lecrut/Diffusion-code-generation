def find_min_element(numbers):
    if not numbers:
        return None
    min_element = numbers[0]
    for number in numbers:
        if number < min_element:
            min_element = number
    return min_element

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_min_element(sample_numbers))