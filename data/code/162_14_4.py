if __name__ == '__main__':
    data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4
    }
    mapped_data = {name: value for name, value in data.items()}
    print(mapped_data)