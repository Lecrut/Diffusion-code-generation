if __name__ == '__main__':
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    result = {key: my_dict[key] for key in my_dict}
    print(result)