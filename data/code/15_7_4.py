if __name__ == '__main__':
    data = {'a': 10, 'b': 20, 'c': 10, 'd': 40}
    key1 = 'a'
    key2 = 'c'
    result = {
        'is_identical': data[key1] == data[key2]
    }
    print(result)