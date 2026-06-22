def find_max_value(numbers):
    if not numbers:
        return None
    return max(numbers)

if __name__ == '__main__':
    sample_values = [7, 3, 9, 2, 5]
    print(find_max_value(sample_values))
    empty_list = []
    print(find_max_value(empty_list))