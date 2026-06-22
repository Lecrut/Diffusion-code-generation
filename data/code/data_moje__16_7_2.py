def get_leading_element(data):
    if not data:
        raise ValueError("List must not be empty")
    return data[0]

if __name__ == '__main__':
    sample_list = [42, 18, 7, 23, 91]
    result = get_leading_element(sample_list)
    print(result)