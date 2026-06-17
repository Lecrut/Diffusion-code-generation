def get_last_value(container, default=None):
    try:
        return container[-1] if len(container) > 0 else default
    except (IndexError, TypeError):
        return default
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    empty_tuple = ()
    single_char_string = "a"
    print(get_last_value(sample_list))
    print(get_last_value(empty_tuple, default="Empty"))
    print(get_last_value(single_char_string))