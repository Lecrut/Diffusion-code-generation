def sum_of_five(a, b, c, d, e):
    total = 0
    for num in [a, b, c, d, e]:
        total += num
    return total

if __name__ == '__main__':
    result = sum_of_five(1, 2, 3, 4, 5)
    print(result)