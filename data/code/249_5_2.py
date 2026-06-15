if __name__ == '__main__':
    data = [15, 8, 22, 4, 30, 11]
    if not data:
        largest = None
    else:
        largest = data[0]
        for number in data[1:]:
            if number > largest:
                largest = number
    print(largest)