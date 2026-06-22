def find_max_value(numbers):
    return max(numbers) if numbers else None
if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_max_value(sample_values))
    empty_list = []
    print(find_max_value(empty_list))