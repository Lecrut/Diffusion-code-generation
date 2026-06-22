def find_max_element(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_list = [2.718, 3.14, 1.618, 0.577, 1.414]
    result = find_max_element(sample_list)
    print(result)