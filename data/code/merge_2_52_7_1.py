import sys
def get_last_element_iterable(iterable):
    iterator = iter(iterable)
    last_item = None
    try:
        for item in iterator:
            last_item = item
    except StopIteration:
        pass
    return last_item if last_item is not None else None
if __name__ == '__main__':
    large_data_list = list(range(10**7))
    result = get_last_element_iterable(large_data_list)
    print(result)