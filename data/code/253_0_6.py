def find_the_middle_value_among_three_transform(a, b, c):
    if a < b:
        if b < c:
            return b
        elif a < c:
            return c
        else:
            return a
    else:
        if a < c:
            return a
        elif b < c:
            return c
        else:
            return b

if __name__ == '__main__':
    print(find_the_middle_value_among_three_transform(5, 3, 4))