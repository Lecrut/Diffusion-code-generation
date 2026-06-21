from operator import itemgetter

def get_last_item(lst):
    if not lst:
        raise IndexError("list is empty")
    getter = itemgetter(-1)
    return getter(lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)