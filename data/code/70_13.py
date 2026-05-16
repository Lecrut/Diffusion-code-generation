if __name__ == '__main__':
    data = ["apple", "banana", "cherry", "date", "elderberry"]
    if len(data) >= 2:
        print(data[0], data[-1])
    elif len(data) == 1:
        print(data[0])
    else:
        print("List is empty")