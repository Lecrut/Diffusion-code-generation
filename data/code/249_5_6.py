if __name__ == '__main__':
    data = [15, 8, 23, 4, 31, 10]
    if not data:
        largest = None
    else:
        largest = data[0]
        for number in data[1:]:
            if number > largest:
                largest = number
    print(largest)