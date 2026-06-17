def get_last_value(container):
    if container:
        return container[-1]
    else:
        raise ValueError("Container is empty")
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = (5, 6)
    sample_string = "hello"
    try:
        print(get_last_value(sample_list))
        print(get_last_value(sample_tuple))
        print(get_last_value(sample_string))
        empty_container = []
        result = get_last_value(empty_container) if False else None
    except ValueError:
        pass
def safe_get_last(container, default=None):
    try:
        return container[-1]
    except IndexError:
        return default
print(safe_get_last(sample_list))
print(safe_get_last(sample_tuple))
print(safe_get_last(sample_string))
print(safe_get_last(empty_container, "DEFAULT"))