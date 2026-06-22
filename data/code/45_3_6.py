def get_minimum_value(numbers):
    return min(numbers) if numbers else None

if __name__ == '__main__':
    sample_list = [10, 5, 23, 1, 45, 12]
    result = get_minimum_value(sample_list)
    print(result)