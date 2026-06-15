if __name__ == '__main__':
    numbers = [10, 25, 32, 48, 55]
    n = len(numbers)
    if n % 2 == 1:
        middle_index = n // 2
        middle_value = numbers[middle_index]
        print(middle_value)
    else:
        middle_left_index = n // 2 - 1
        middle_right_index = n // 2
        middle_left_value = numbers[middle_left_index]
        middle_right_value = numbers[middle_right_index]
        middle_value = (middle_left_value + middle_right_value) / 2
        print(middle_value)