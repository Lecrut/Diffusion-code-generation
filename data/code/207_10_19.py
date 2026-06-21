def find_max_element(numbers):
    max_value = float('-inf')
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

if __name__ == '__main__':
    sample_values = [10, 7, 23, 5, 15]
    print(find_max_element(sample_values))