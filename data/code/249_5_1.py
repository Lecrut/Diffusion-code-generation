if __name__ == '__main__':
    data = [15, 8, 22, 4, 30, 11]
    if not data:
        largest = None
    else:
        largest = data[0]
        for i in range(1, len(data)):
            if data[i] > largest:
                largest = data[i]
    print(largest)