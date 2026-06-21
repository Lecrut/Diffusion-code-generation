def get_last_element(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)
    sample_mixed = ["apple", 3.14, True, 100]
    result_mixed = get_last_element(sample_mixed)
    print(result_mixed)