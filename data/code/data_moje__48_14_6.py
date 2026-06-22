def find_max_custom(data):
    if not data:
        return None
    max_val = data[0]
    for num in data[1:]:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == '__main__':
    sample_data = [3.5, 7.2, 1.8, 9.4, 6.1, 9.4]
    result = find_max_custom(sample_data)
    print(result)