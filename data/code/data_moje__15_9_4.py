def get_penultimate_element(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) < 2:
        raise ValueError("List must contain at least two elements")
    return data[-2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_penultimate_element(sample_list))
    another_list = ["a", "b", "c"]
    print(get_penultimate_element(another_list))