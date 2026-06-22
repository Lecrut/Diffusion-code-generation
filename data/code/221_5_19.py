def sort_three_numbers(a, b, c):
    if a <= b and a <= c:
        first = a
        if b <= c:
            second = b
            third = c
        else:
            second = c
            third = b
    elif b <= a and b <= c:
        first = b
        if a <= c:
            second = a
            third = c
        else:
            second = c
            third = a
    else:
        first = c
        if a <= b:
            second = a
            third = b
        else:
            second = b
            third = a
    return first, second, third

if __name__ == '__main__':
    sample_values = [5, 2, 8]
    sorted_values = sort_three_numbers(*sample_values)
    print(sorted_values)

    sample_values_2 = [100, 1, 50]
    sorted_values_2 = sort_three_numbers(*sample_values_2)
    print(sorted_values_2)

    sample_values_3 = [3, 3, 3]
    sorted_values_3 = sort_three_numbers(*sample_values_3)
    print(sorted_values_3)