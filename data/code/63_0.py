def find_first_element(data):
    if not data:
        return None
    return data[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    first_value = find_first_element(sample_list)
    print(first_value)