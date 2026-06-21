from operator import itemgetter

def get_last_item(lst):
    if not lst:
        raise IndexError("list index out of range")
    return itemgetter(-1)(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_last_item(sample_list))