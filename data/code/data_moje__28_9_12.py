def sort_two_numbers(a, b):
    if a < b:
        return a, b
    return b, a

if __name__ == '__main__':
    x = 3.14
    y = 2.71
    sorted_x, sorted_y = sort_two_numbers(x, y)
    print(sorted_x)
    print(sorted_y)