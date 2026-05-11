if __name__ == '__main__':
    data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    value_map = {name: data[name] for name in data}
    print(value_map)