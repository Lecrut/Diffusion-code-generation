def is_max_greater_than_second_to_last(numbers):
    if len(numbers) < 2:
        return False
    max_value = max(numbers)
    second_to_last_value = numbers[-2]
    return max_value > second_to_last_value

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = is_max_greater_than_second_to_last(sample_values)
    print(result)