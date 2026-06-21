def find_max_element(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [7, 3, 9, 1, 5]
    print(find_max_element(sample_values))