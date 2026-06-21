def get_max_element(data_set):
    if not data_set:
        raise ValueError("Input set cannot be empty")
    max_value = data_set[0]
    for value in data_set[1:]:
        if value > max_value:
            max_value = value
    return max_value

if __name__ == '__main__':
    sample_data = {4, 8, 15, 16, 23, 42}
    print(f"The maximum element is: {get_max_element(sample_data)}")