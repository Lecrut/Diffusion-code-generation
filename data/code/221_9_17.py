def sort_three_numbers(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    return a, b, c

if __name__ == '__main__':
    sample_values = (10, 3, 7)
    sorted_numbers = sort_three_numbers(*sample_values)
    print(sorted_numbers)