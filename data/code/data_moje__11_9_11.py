import operator

def get_last_item(lst):
    if not lst:
        return None
    return operator.itemgetter(-1)(lst)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_last_item(sample_data)
    print(result)