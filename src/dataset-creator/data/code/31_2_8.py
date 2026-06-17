def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    store = {'a': 10, 'b': 20, 'c': 30}
    result_a = get_value(store, 'a')
    result_b = get_value(store, 'd')
    print(f"Value for a: {result_a}")