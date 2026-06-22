def get_first_element(data):
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError("Input must be a non-empty list")
    return data[0]

if __name__ == '__main__':
    sample_data = [5, 10, 15]
    print(get_first_element(sample_data))