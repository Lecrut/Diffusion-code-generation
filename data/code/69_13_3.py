if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_middle = numbers[0:4:2]
    middle_last = numbers[2:8:3]
    last_three = numbers[-3:]
    print(f"First, middle, and last three elements:")
    print(f"First/Middle (using slice 0:4:2): {first_middle}")
    print(f"Middle/Last (using slice 2:8:3): {middle_last}")
    print(f"Last three (using slice -3:): {last_three}")