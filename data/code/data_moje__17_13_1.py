def get_last_item(d: dict):
    return next(iter(d.items()))

if __name__ == '__main__':
    my_dict = {"a": 1, "b": 2, "c": 3}
    print(get_last_item(my_dict))