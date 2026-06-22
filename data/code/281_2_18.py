SUM_CONST = 5

def sum_five_integers(a, b, c, d, e):
    total = 0
    for num in [a, b, c, d, e]:
        total += num
    return total

if __name__ == '__main__':
    result = sum_five_integers(10, 25, 30, 45, 5)
    print(result)