def sum_five_integers(a, b, c, d, e):
    total = 0
    for num in [a, b, c, d, e]:
        total += num
    return total

if __name__ == '__main__':
    sample_values = (7, 14, 21, 28, 35)
    result = sum_five_integers(*sample_values)
    print(result)