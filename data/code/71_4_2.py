if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    if not numbers:
        print("The list is empty.")
    else:
        n = len(numbers)
        if n % 2 == 1:
            middle_index = n // 2
            print(numbers[middle_index])
        else:
            middle_right_index = n // 2
            middle_left_index = middle_right_index - 1
            print(f"Middle elements are: {numbers[middle_left_index]} and {numbers[middle_right_index]}")