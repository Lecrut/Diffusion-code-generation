def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    num1, num2, num3 = 4.56, 7.89, 1.23
    sorted_numbers = sort_three_numbers(num1, num2, num3)
    print(sorted_numbers)