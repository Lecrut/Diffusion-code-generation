def get_last_value(container, default=None):
    try:
        return container[-1]
    except IndexError:
        return default
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    empty_tuple = ()
    string_seq = "hello"
    result_list = get_last_value(sample_list)
    result_empty = get_last_value(empty_tuple, default="N/A")
    result_string = get_last_value(string_seq)
    print(f"List last: {result_list}")
    print(f"Empty tuple last: {result_empty}")
    print(f"String last: '{result_string}'")