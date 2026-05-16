if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_middle = numbers[0:4:2]
    middle = numbers[3:7]
    last = numbers[-3:]
    print(f"First, Middle, and Last three elements:")
    print(f"First and Middle (using slicing): {first_middle}")
    print(f"Middle (using slicing): {middle}")
    print(f"Last three (using slicing): {last}")