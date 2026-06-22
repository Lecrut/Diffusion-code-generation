def get_first_element(data):
    if not data:
        raise ValueError("The provided list is empty.")
    return data[0]

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True]
    result = get_first_element(sample_list)
    print(result)