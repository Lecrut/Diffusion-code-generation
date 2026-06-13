if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    n = len(data)
    largest = data[0]
    for i in range(1, n):
        if data[i] > largest:
            largest = data[i]
    print(largest)