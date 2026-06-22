def find_max_number(numbers):
    max_value = float('-inf')
    for number in numbers.split():
        if float(number) > max_value:
            max_value = float(number)
    return max_value

if __name__ == '__main__':
    sample_input = "3.14159 2.71828 1.61803 4.0 0.5"
    maximum = find_max_number(sample_input)
    print(maximum)