def get_last_value(container, default=None):
    if container:
        return container[-1]
    return default
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 'a', True)
    sample_string = "hello"
    empty_list = []
    print(get_last_value(sample_list))
    print(get_last_value(sample_tuple))
    print(get_last_value(sample_string))
    print(get_last_value(empty_list, default="EMPTY"))