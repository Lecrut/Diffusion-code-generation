def find_max_value(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [7, 12, 3, 5, 9]
    largest = find_max_value(sample_values)
    print(largest)

    empty_list = []
    result = find_max_value(empty_list)
    print(result)