if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_middle = numbers[0:4:2]
    middle_last = numbers[2:7]
    last_three = numbers[-3:]
    print(f"First, middle, and last three elements extracted:")
    print(f"First and middle (with step): {first_middle}")
    print(f"Middle section: {middle_last}")
    print(f"Last three: {last_three}")