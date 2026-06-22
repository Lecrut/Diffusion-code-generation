def find_max_value(numbers):
    return max(numbers) if numbers else None

if __name__ == '__main__':
    sample_values = [12, 45, 32, 78, 90]
    print(find_max_value(sample_values))
    empty_list = []
    print(find_max_value(empty_list))