if __name__ == '__main__':
    data = [1, 2, 3, 4, 2, 5, 2]
    target = 2
    result = -1
    for i in range(len(data) - 1, -1, -1):
        if data[i] == target:
            result = i
            break
    print(result)