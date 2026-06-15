if __name__ == '__main__':
    data = [15, 8, 23, 4, 31, 10]
    if not data:
        largest = None
    else:
        largest = data[0]
        for i in range(1, len(data)):
            if data[i] > largest:
                largest = data[i]
    print(largest)