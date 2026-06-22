def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    sample_values = (10, 5, 8)
    sorted_numbers = sort_three_numbers(*sample_values)
    print(sorted_numbers)