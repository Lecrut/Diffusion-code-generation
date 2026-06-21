import operator

def get_last_item(lst):
    if not lst:
        raise ValueError('List must not be empty')
    return operator.itemgetter(-1)(lst)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)