import operator

def get_last_item(input_list):
    last_index = -1
    getter = operator.itemgetter(last_index)
    return getter(input_list)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)