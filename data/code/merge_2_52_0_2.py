def get_last_value(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    samples = [10, 20, 30], ['a', 'b', 'c'], [], [[1, 2], [3]]
    for sample in samples:
        result = get_last_value(sample)
        print(result)