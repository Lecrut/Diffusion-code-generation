def sort_two_numbers(a, b):
    first_number = a
    second_number = b
    if first_number > second_number:
        first_number, second_number = second_number, first_number
    return [first_number, second_number]

if __name__ == '__main__':
    x = 42
    y = -7
    result = sort_two_numbers(x, y)
    print(result)