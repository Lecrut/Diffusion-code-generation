if __name__ == '__main__':
    START_RANGE = 0
    END_RANGE = 50

    even_numbers = [num for num in range(START_RANGE, END_RANGE + 1) if num % 2 == 0]
    print(even_numbers)