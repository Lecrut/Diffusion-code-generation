from collections import OrderedDict

def get_last_key_value(data):
    if not data:
        return None
    return list(data.items())[-1]

if __name__ == '__main__':
    sample_dict = OrderedDict([('first', 10), ('second', 20), ('third', 30)])
    result = get_last_key_value(sample_dict)
    print(result)