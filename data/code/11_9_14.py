import operator

_LAST_ITEM_INDEX = -1

def retrieve_last_element(sequence):
    accessor = operator.itemgetter(_LAST_ITEM_INDEX)
    return accessor(sequence)

if __name__ == '__main__':
    data_collection = ["alpha", "beta", "gamma"]
    output = retrieve_last_element(data_collection)
    print(output)