def get_last_item(d):
    items = list(d.items())
    return items[-1]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_last_item(sample_dict))