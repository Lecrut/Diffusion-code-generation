if __name__ == '__main__':
    data = [12, 45, 67, 89, 34]
    if not data:
        largest = None
    else:
        largest = data[0]
        for number in data[1:]:
            if number > largest:
                largest = number
    print(largest)