import operator

def get_last_item(lst):
    if not lst:
        raise IndexError("Cannot get the last item of an empty list")
    get_last = operator.itemgetter(-1)
    return get_last(lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)