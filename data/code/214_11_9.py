def find_min_element(numbers):
    if not numbers:
        return None
    min_element = numbers[0]
    for number in numbers:
        if number < min_element:
            min_element = number
    return min_element

if __name__ == '__main__':
    sample_numbers = [34, 78, 12, 56, 90, 23, 67]
    print(find_min_element(sample_numbers))