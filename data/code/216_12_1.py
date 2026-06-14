if __name__ == '__main__':
    sequence = [10, 20, 30, 40, 50]
    n = len(sequence)
    if n % 2 == 1:
        middle_index = n // 2
        middle_value = sequence[middle_index]
        print(middle_value)
    else:
        middle_left_index = n // 2 - 1
        middle_right_index = n // 2
        middle_left_value = sequence[middle_left_index]
        middle_right_value = sequence[middle_right_index]
        middle_value = (middle_left_value + middle_right_value) / 2
        print(middle_value)