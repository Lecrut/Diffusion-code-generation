def get_nested_dict_values(data, keys):
    if not isinstance(data, dict) or not all((isinstance(k, str) and k in data for k in keys)):
        raise ValueError("Invalid input: 'data' must be a dictionary and 'keys' must be a list of existing string keys.")
    return [data[key] for key in keys]
if __name__ == '__main__':
    nested_dict = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': {'g': 4}, 'h': 5}}
    keys = ['b', 'd', 'g']
    result = get_nested_dict_values(nested_dict, keys)
    print(result)