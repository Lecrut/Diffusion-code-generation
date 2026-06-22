def get_first_item(data_tuple):
    first_item, *_ = data_tuple
    return first_item

if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = get_first_item(sample_tuple)
    print(result)