def get_last_element(data):
    if not data:
        raise ValueError("List is empty")
    return data[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_element(sample_list))