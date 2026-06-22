def get_last_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 42, 99]
    result = get_last_element(sample_list)
    print(result)