def get_first_item(data):
    return data[0]
if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, [1, 2]]
    first_value = get_first_item(sample_list)
    print(first_value)