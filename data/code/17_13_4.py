def get_last_key_value(d):
    return next(iter(d.items()))

if __name__ == '__main__':
    my_dict = {1: 'a', 2: 'b', 3: 'c'}
    print(get_last_key_value(my_dict))