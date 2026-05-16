if __name__ == '__main__':
    data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    result = {name: value for name, value in data.items()}
    print(result)