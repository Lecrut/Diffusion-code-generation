if __name__ == '__main__':
    data = [10, 3.14, 5, 22.9, -1.5]
    largest = data[0]
    for item in data:
        if item > largest:
            largest = item
    print(largest)