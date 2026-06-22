def sort_three(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

if __name__ == '__main__':
    sorted_numbers = sort_three(15, 3, 9)
    print(f"Sorting (15, 3, 9): {sorted_numbers}")