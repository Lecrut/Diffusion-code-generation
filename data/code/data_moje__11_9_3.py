import operator

def get_last_item(items):
    if not items:
        raise IndexError("Cannot get last item from an empty list")
    getter = operator.itemgetter(-1)
    return getter(items)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)