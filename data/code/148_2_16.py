def find_largest_element(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    sample_data = [10.5, 7.2, 3.8, 15.4, 9.9]
    result = find_largest_element(sample_data)
    print(result)