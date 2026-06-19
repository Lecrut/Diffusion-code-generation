def is_max_greater_than_penultimate(numbers):
    if len(numbers) < 2:
        return False
    max_value = max(numbers)
    second_to_last = numbers[-2]
    return max_value > second_to_last

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = is_max_greater_than_penultimate(sample_values)
    print(result)