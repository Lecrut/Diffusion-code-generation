def sort_three_numbers(a, b, c):
    if a <= b:
        if a <= c:
            smallest = a
            if b <= c:
                middle = b
                largest = c
            else:
                middle = c
                largest = b
        else:
            smallest = c
            middle = a
            largest = b
    else:
        if a <= c:
            smallest = b
            middle = a
            largest = c
        else:
            smallest = b
            if a <= c:
                middle = a
                largest = c
            else:
                middle = c
                largest = a

    return smallest, middle, largest

if __name__ == '__main__':
    sample_values = (10, 5, 7)
    sorted_values = sort_three_numbers(*sample_values)
    print(sorted_values)