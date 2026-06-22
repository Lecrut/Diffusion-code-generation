def sort_three_numbers(a, b, c):
    if a <= b <= c:
        return a, b, c
    elif a <= c <= b:
        return a, c, b
    elif b <= a <= c:
        return b, a, c
    elif b <= c <= a:
        return b, c, a
    elif c <= a <= b:
        return c, a, b
    else:
        return c, b, a

if __name__ == '__main__':
    sample_values = [5, 2, 8]
    print(sort_three_numbers(*sample_values))
    sample_values_2 = [100, 1, 50]
    print(sort_three_numbers(*sample_values_2))
    sample_values_3 = [3, 3, 3]
    print(sort_three_numbers(*sample_values_3))