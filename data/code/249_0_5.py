def find_max_value(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(find_max_value(sample_values))
    empty_list = []
    result = find_max_value(empty_list)
    print(result)