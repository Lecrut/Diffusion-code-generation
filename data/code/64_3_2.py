if __name__ == '__main__':
    data = [1, 2, 3, 4, 4, 5, 4]
    target = 4
    last_index = data.index(target) if target in data else -1
    print(last_index)