from collections import OrderedDict

def get_last_item(input_dict):
    if not input_dict:
        return None
    items = list(input_dict.items())
    return items[-1]

if __name__ == '__main__':
    sample_dict = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
    result = get_last_item(sample_dict)
    print(result)