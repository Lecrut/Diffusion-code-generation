def sum_of_five(a, b, c, d, e):
    total = 0
    numbers = [a, b, c, d, e]
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    result = sum_of_five(10, 25, 30, 45, 5)
    print(result)