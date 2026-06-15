if __name__ == '__main__':
    data = [5, 2, 8, 1, 9]
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swapped = True
    print(data)