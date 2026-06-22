def get_first_item(iterable):
    try:
        return iter(iterable).__next__()
    except StopIteration:
        return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_tuple = (5, 6, 7, 8)
    sample_string = "Alibaba"
    empty_dict = {}

    print(get_first_item(sample_list))
    print(get_first_item(sample_tuple))
    print(get_first_item(sample_string))
    print(get_first_item(empty_dict))