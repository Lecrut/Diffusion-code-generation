def count_elements(data):
    if isinstance(data, list):
        total = 0
        for item in data:
            total += count_elements(item)
        return total
    else:
        return 1
if __name__ == '__main__':
    sample_data = [1, 'a', {'b': [2, 3], 'c': [[4]]}, True]
    result = count_elements(sample_data)
    print(result)