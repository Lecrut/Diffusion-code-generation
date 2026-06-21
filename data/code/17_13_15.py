from collections import OrderedDict

EMPTY_DICT_THRESHOLD = 0

def retrieve_final_pair(mapping):
    if len(mapping) <= EMPTY_DICT_THRESHOLD:
        raise ValueError("Input dictionary must not be empty")
    last_item = next(reversed(mapping.items()))
    return last_item

if __name__ == '__main__':
    ordered_data = OrderedDict()
    ordered_data['first_entry'] = 100
    ordered_data['second_entry'] = 200
    ordered_data['final_entry'] = 300
    result = retrieve_final_pair(ordered_data)
    print(result)