def assign_numbers(a, b, c):
    if a < b:
        if a < c:
            if b < c:
                return a, b, c
            else:
                return a, c, b
        else:
            return c, a, b
    else:
        if a < c:
            return b, a, c
        elif b < c:
            return b, c, a
        else:
            return c, b, a

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    sorted_nums = assign_numbers(num1, num2, num3)
    print(f"Sorted numbers: {sorted_nums}")