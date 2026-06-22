def count_non_matching_elements(data, target_type):
    non_matching_count = 0
    for item in data:
        if not isinstance(item, target_type):
            non_matching_count += 1
    return non_matching_count
if __name__ == '__main__':
    sample_data = [3.14, True, 'hello', 2.718]
    result = count_non_matching_elements(sample_data, float)
    print(result)