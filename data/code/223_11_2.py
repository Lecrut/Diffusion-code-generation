def find_max_element(numbers):
    max_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

if __name__ == '__main__':
    sample_values = [3.14, 2.71, 1.618, 0.577, 1.414]
    print(find_max_element(sample_values))