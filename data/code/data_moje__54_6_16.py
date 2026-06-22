def hollow_square(n: int) -> str:
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    first_row = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    return "\n".join([first_row] + [middle_row] * (n - 2) + [first_row])

if __name__ == '__main__':
    size = 7
    print(hollow_square(size))