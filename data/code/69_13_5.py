if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_middle = data[0:4:2]
    middle = data[3:7]
    last = data[-3:]
    print(f"First, Middle, and Last three elements:")
    print(f"First (with step): {first_middle}")
    print(f"Middle (slice): {middle}")
    print(f"Last three (slice): {last}")