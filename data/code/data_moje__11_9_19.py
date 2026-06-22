import operator

def get_last_item(lst):
    if not lst:
        raise IndexError('list index out of range')
    last_index = len(lst) - 1
    return operator.itemgetter(last_index)(lst)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)