def find_max_value(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [34, 56, 23, 89, 12]
    result = find_max_value(sample_values)
    print(result)

    empty_list = []
    result = find_max_value(empty_list)
    print(result)