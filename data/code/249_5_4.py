if __name__ == '__main__':
    data = [12, 45, 67, 89, 34]
    if not data:
        largest = None
    else:
        largest = data[0]
        for i in range(1, len(data)):
            if data[i] > largest:
                largest = data[i]
    print(largest)