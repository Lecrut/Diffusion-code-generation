if __name__ == '__main__':
    data = [10, 5, 20, 8, 15]
    if not data:
        print("List is empty")
    else:
        largest = data[0]
        for x in data:
            if x > largest:
                largest = x
        print(largest)