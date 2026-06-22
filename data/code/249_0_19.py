def find_largest_value(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [12, 45, 78, 3, 90]
    largest = find_largest_value(sample_values)
    print(largest)

    empty_list = []
    result = find_largest_value(empty_list)
    print(result)