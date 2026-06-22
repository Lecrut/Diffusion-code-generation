def get_max_from_dict(d):
    return max(d.values())

if __name__ == '__main__':
    data = {'a': 10, 'b': 42, 'c': 7, 'd': 33}
    result = get_max_from_dict(data)
    print(result)