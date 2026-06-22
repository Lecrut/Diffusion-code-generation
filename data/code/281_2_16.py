def sum_five_integers(a, b, c, d, e):
    total = 0
    for number in (a, b, c, d, e):
        total += number
    return total

if __name__ == '__main__':
    result = sum_five_integers(10, 25, 30, 5, 1)
    print(result)