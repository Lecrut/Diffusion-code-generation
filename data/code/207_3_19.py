MAX_VALUE_KEY = 'max_value'

def find_highest_value(data_dict):
    return max(data_dict.values(), key=lambda x: x.get(MAX_VALUE_KEY))

if __name__ == '__main__':
    sample_data = {
        'item1': {'price': 20, MAX_VALUE_KEY: True},
        'item2': {'price': 15, MAX_VALUE_KEY: False},
        'item3': {'price': 30, MAX_VALUE_KEY: True}
    }
    result = find_highest_value(sample_data)
    print(result['price'])