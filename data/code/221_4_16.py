def sort_three_numbers(a, b, c):
    if a > b:
        a, b = (b, a)
    if b > c:
        b, c = (c, b)
    if a > b:
        a, b = (b, a)
    return (a, b, c)
if __name__ == '__main__':
    result = sort_three_numbers(3.5, 1.2, 2.8)
    print(result)