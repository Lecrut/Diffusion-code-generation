def get_third_item(data):
    try:
        return data[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_third_item(sample_list))
    empty_list = []
    print(get_third_item(empty_list))