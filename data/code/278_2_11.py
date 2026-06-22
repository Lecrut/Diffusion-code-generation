def print_integers(integer_list):
    index = 0
    while index < len(integer_list):
        if not isinstance(integer_list[index], int):
            raise ValueError("All elements in the list must be integers.")
        print(integer_list[index])
        index += 1

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    try:
        print_integers(sample_values)
    except ValueError as e:
        print(e)