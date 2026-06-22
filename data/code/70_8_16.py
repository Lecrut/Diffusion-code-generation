FIRST = 0
LAST = -1

def check_endpoints(iterable):
    try:
        items = list(iterable)
    except TypeError:
        raise ValueError("Input must be an iterable")
    if len(items) == 0:
        return None, None
    return items[FIRST], items[LAST]

if __name__ == '__main__':
    data = [10, 20, 30]
    print(check_endpoints(data))
    empty_data = []
    print(check_endpoints(empty_data))
    text = "test"
    print(check_endpoints(text))