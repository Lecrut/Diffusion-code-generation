def get_first_element(data):
    try:
        return data[0]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [7, 14, 21, 28]
    print(get_first_element(sample_list))