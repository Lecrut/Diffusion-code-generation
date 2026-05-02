if __name__ == '__main__':
    data = [1, 2, 3, 4, 4, 5]
    target = 4
    result = data.index(target) if target in data else -1
    print(result)