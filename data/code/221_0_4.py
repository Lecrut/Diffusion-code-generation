def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    numbers = [15, 9, 21]
    sorted_numbers = sort_three_numbers(*numbers)
    print(sorted_numbers[0], sorted_numbers[1], sorted_numbers[2])