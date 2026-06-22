def print_star_square(size):
    if size <= 0:
        return
    if size == 1:
        print("*")
        return

    first_last = "*" * size
    middle_row = "*" + " " * (size - 2) + "*"

    print(first_last)
    for _ in range(size - 2):
        print(middle_row)
    print(first_last)

if __name__ == '__main__':
    print_star_square(5)