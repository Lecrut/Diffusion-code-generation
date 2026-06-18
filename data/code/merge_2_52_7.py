import sys
def get_last_element(iterable):
    iterator = iter(iterable)
    last_item = None
    for item in iterator:
        last_item = item
    return last_item
if __name__ == '__main__':
    large_data = list(range(10_000_000))
    result = get_last_element(large_data)
    print(result)