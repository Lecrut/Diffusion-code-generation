def extract_third_value(data):
    if len(data) < 3:
        raise IndexError('List must contain at least three elements.')
    return data[2]
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = extract_third_value(sample_data)
    print(result)