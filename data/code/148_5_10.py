def find_greatest_element(numbers):
    if not numbers:
        return None
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4, 8, 6, 7]
    print(find_greatest_element(sample_values))