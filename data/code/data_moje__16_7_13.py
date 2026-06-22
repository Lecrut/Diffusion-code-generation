def get_leading_element(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_leading_element(sample_list)
    print(result)