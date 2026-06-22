sample_values = {
    'pi': 3.14,
    'e': 2.718,
    'phi': 1.618,
    'gamma': 0.577,
    'sqrt_2': 1.414
}

def find_max_element(numbers):
    max_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
    return max_element

if __name__ == '__main__':
    sample_list = list(sample_values.values())
    result = find_max_element(sample_list)
    print(result)