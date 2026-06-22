def sort_three_numbers(a, b, c):
    if a <= b:
        if a <= c:
            if b <= c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    else:
        if a <= c:
            return b, a, c
        elif b <= c:
            return b, c, a
        else:
            return c, b, a

if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(3, 1, 2)
    print(sorted_numbers)