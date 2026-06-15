if __name__ == '__main__':
    sequence = [10, 20, 30, 40, 50]
    n = len(sequence)
    if n % 2 == 1:
        middle_index = n // 2
        middle_value = sequence[middle_index]
        print(middle_value)
    else:
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        middle_value_1 = sequence[middle_index_1]
        middle_value_2 = sequence[middle_index_2]
        print(f"{middle_value_1}, {middle_value_2}")