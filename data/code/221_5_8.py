def sort_three_numbers(a, b, c):
    if a <= b and a <= c:
        smallest = a
        if b <= c:
            middle = b
            largest = c
        else:
            middle = c
            largest = b
    elif b <= a and b <= c:
        smallest = b
        if a <= c:
            middle = a
            largest = c
        else:
            middle = c
            largest = a
    else:
        smallest = c
        if a <= b:
            middle = a
            largest = b
        else:
            middle = b
            largest = a

    return smallest, middle, largest

if __name__ == '__main__':
    sample_values = (5, 2, 8)
    sorted_values = sort_three_numbers(*sample_values)
    print(sorted_values)