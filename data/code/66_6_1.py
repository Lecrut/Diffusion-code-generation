def kilometers_to_meters():
    inputs = [1, 5, 10, 25, 50]
    for km in inputs:
        yield km * 1000

if __name__ == '__main__':
    for value in kilometers_to_meters():
        print(value)