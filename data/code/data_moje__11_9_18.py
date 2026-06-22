import operator

def get_last_item(data):
    return operator.itemgetter(-1)(data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)