def count_elements_from_start(data):
    if data is None:
        return 0
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    count = len(data)
    return count
if __name__ == '__main__':
    sample_data = [1, 2, 3, None]
    result = count_elements_from_start(sample_data)
    print(result)