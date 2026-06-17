def get_value(data: dict, key) -> any:
    return data.get(key)
if __name__ == '__main__':
    sample_data = {'apple': 10, 'banana': 20, 'cherry': 30}
    result = get_value(sample_data, 'banana')
    print(result)