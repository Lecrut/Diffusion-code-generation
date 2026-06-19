def is_max_greater_than_second_to_last(numbers):
    if len(numbers) < 2:
        return False
    max_value = max(numbers)
    second_to_last_value = numbers[-2]
    return max_value > second_to_last_value

if __name__ == '__main__':
    sample_list = [3, 5, 1, 8, 7]
    result = is_max_greater_than_second_to_last(sample_list)
    print(result)