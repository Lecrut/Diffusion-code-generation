import operator

def get_last_item(lst):
    getter = operator.itemgetter(-1)
    return getter(lst)

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45, 60]
    result = get_last_item(sample_list)
    print(result)