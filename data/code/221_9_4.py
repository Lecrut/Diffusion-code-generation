def custom_sort(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                return a, c, b
            else:
                return a, b, c
        else:
            if b > c:
                return c, a, b
            else:
                return c, b, a
    else:
        if b > a:
            if b > c:
                if a > c:
                    return b, a, c
                else:
                    return b, c, a
            else:
                if a > c:
                    return b, c, a
                else:
                    return b, a, c
        else:
            if a > c:
                return a, b, c
            else:
                return c, b, a
if __name__ == '__main__':
    numbers = [15, 8, 22]
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    sorted_a, sorted_b, sorted_c = custom_sort(a, b, c)
    print(f"Original numbers: {numbers}")
    print(f"Sorted numbers: {sorted_a}, {sorted_b}, {sorted_c}")