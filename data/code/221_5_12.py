def sort_three_numbers(a, b, c):
    if a <= b:
        if b <= c:
            print(a, b, c)
        else:
            if a <= c:
                print(a, c, b)
            else:
                print(c, a, b)
    else:
        if a <= c:
            print(b, a, c)
        else:
            if b <= c:
                print(b, c, a)
            else:
                print(c, b, a)

if __name__ == '__main__':
    sort_three_numbers(3, 1, 2)