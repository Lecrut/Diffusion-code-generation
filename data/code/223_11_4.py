def find_max_element(numbers):
    max_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

if __name__ == '__main__':
    sample_numbers = [3.5, 1.2, 7.8, 4.9, 2.1]
    print(find_max_element(sample_numbers))