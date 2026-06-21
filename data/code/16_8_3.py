def yield_first_value():
    vector = [10, 20, 30, 40, 50]
    for item in vector:
        return item

if __name__ == '__main__':
    print(yield_first_value())