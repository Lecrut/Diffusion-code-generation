def find_max_value(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [3.14, 2.718, 1.618, 0.577, -1]
    print(find_max_value(sample_values))