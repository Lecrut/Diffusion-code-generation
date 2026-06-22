def sort_two_numbers(a, b):
    if a <= b:
        return a, b
    else:
        return b, a

if __name__ == '__main__':
    x = 3.14
    y = 2.71
    sorted_values = sort_two_numbers(x, y)
    print(sorted_values[0])
    print(sorted_values[1])