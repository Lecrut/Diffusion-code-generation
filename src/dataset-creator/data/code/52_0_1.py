def get_last_value(data):
    if not data:
        return None
    return data[-1]
if __name__ == '__main__':
    samples = [30, 40, 50], ['a', 'b', 'c'], [[1, 2], [3]], []
    for sample in samples:
        print(get_last_value(sample))