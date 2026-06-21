def find_max_mixed(numbers):
    max_value = float('-inf')
    for num in numbers:
        if isinstance(num, (int, float)):
            if num > max_value:
                max_value = num
    return int(max_value) if isinstance(max_value, float) and max_value.is_integer() else max_value

if __name__ == '__main__':
    sample_values = [3, 5.7, 2, 'a', None, 8]
    print(find_max_mixed(sample_values))