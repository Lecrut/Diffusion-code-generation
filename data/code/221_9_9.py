def sort_three(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return a, b, c

if __name__ == '__main__':
    result = sort_three(3, 1, 2)
    print(result)