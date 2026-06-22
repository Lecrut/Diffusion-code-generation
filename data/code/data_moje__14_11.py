def get_third_item(data):
    if len(data) > 2:
        return data[2]
    return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    print(get_third_item(sample_list))