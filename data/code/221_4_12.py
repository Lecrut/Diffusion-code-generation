def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    result = sort_three_numbers(4.56, 3.21, 2.89)
    print(result)