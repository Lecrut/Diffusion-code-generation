def find_max_mixed(numbers):
    max_value = None
    for number in numbers:
        if isinstance(number, (int, float)):
            if max_value is None or number > max_value:
                max_value = number
    return max_value

if __name__ == '__main__':
    sample_values = [3.5, 10, 2, "a", 7]
    print(find_max_mixed(sample_values))