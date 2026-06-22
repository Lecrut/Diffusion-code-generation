def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(10, 5, 8)
    print(*sorted_numbers)