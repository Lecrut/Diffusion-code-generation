if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_middle = data[0:4:2]
    middle_last = data[2:8:3]
    last_three = data[-3:]
    print(f"First, middle, and last three elements:")
    print(f"First and middle (using slicing): {first_middle}")
    print(f"Middle and last (using slicing): {middle_last}")
    print(f"Last three elements: {last_three}")