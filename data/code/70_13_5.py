if __name__ == '__main__':
    data = [10]
    if len(data) > 1:
        print(data[0], data[-1])
    elif data:
        print(data[0])
    else:
        print("List is empty")