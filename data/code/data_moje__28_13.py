def sort_two_numbers(a, b):
    if a > b:
        return b, a
    return a, b

if __name__ == '__main__':
    x = 15
    y = 4
    sorted_values = sort_two_numbers(x, y)
    print(sorted_values)