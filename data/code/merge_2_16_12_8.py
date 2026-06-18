def count_elements(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list.")
    return len(data)
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result = count_elements(sample_data)
    print(result)