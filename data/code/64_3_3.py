if __name__ == '__main__':
    data = [1, 2, 3, 4, 4, 5, 4]
    target = 4
    index = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == target:
            index = i
            break
    print(index)