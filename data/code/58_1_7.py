def get_first_element(data):
    return data[0] if data else None

if __name__ == '__main__':
    SAMPLE_LIST = [7, 14, 21, 28]
    first_element = get_first_element(SAMPLE_LIST)
    print(first_element)