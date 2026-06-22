def greater_of_two(a, b):
    diff = a - b
    is_positive = (diff >> 31) & 1
    return a if is_positive else b

if __name__ == '__main__':
    first_number = 75
    second_number = 60
    max_value = greater_of_two(first_number, second_number)
    print(max_value)