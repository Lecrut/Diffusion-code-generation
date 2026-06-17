if __name__ == '__main__':
    data = [12, 45, 6, 89, 33, 71]
    if not data:
        largest = None
    else:
        largest = data[0]
        for i in range(1, len(data)):
            if data[i] > largest:
                largest = data[i]
    print(largest)