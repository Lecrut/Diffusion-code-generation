def sort_two_numbers(a, b):
    if a <= b:
        return a, b
    return b, a

if __name__ == '__main__':
    value1 = 42
    value2 = 7
    sorted_values = sort_two_numbers(value1, value2)
    print(sorted_values)