def find_max_with_index(numbers):
    max_value = numbers[0]
    max_index = 0
    for index, value in enumerate(numbers):
        if value > max_value:
            max_value = value
            max_index = index
    return (max_value, max_index)

if __name__ == '__main__':
    sample_numbers = [12, 45, 78, 3, 90]
    result = find_max_with_index(sample_numbers)
    print(f"Max value: {result[0]}, Index: {result[1]}")