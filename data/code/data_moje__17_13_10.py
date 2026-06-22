def get_last_item(d):
    return list(d.items())[-1]

if __name__ == '__main__':
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    print(get_last_item(sample_dict))