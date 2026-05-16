if __name__ == '__main__':
    data = [3, 1, 8, 4, 5, 2]
    if not data:
        largest = None
    else:
        largest = data[0]
        for i in range(1, len(data)):
            if data[i] > largest:
                largest = data[i]
    print(largest)