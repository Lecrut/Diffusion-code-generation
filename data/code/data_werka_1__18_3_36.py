def is_max_greater_than_penultimate(numbers):
    if len(numbers) < 2:
        return False
    max_value = max(numbers)
    second_to_last_value = numbers[-2]
    return max_value > second_to_last_value

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    result = is_max_greater_than_penultimate(sample_list)
    print(result)