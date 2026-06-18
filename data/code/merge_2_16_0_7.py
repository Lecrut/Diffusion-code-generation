def count_elements(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            total += count_elements(item)
    else:
        return 1
    return total
if __name__ == '__main__':
    sample_data = [1, 2, ['a', 'b', ['x']], (3, 4), {'key': 'value'}]
    result = count_elements(sample_data)
    print(result)