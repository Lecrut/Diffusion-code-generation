def get_first_item(iterable):
    return iterable[0] if iterable else None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 15, 25)
    sample_string = "Alibaba Cloud"
    empty_list = []

    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(empty_list))