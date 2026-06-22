def sort_three_numbers(a, b, c):
    if a > b:
        temp = a
        a = b
        b = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = a
        a = b
        b = temp
    return (a, b, c)
if __name__ == '__main__':
    sorted_numbers = sort_three_numbers(3, 1, 2)
    print(sorted_numbers)