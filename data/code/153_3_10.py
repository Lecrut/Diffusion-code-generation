def any_match(data, target):
    return any(item == target for item in data)

if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = any_match(sample_list, target_value)
    print(result)