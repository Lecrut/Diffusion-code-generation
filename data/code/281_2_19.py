def sum_of_five(a, b, c, d, e):
    total = 0
    for value in [a, b, c, d, e]:
        total += value
    return total

if __name__ == '__main__':
    sample_values = (15, 20, 25, 30, 35)
    result = sum_of_five(*sample_values)
    print(result)