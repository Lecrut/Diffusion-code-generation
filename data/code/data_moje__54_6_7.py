def hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    middle_row_str = middle
    middle_part = (middle_row_str + "\n") * (n - 2)
    result = top_bottom + "\n" + middle_part + top_bottom
    return result

if __name__ == '__main__':
    print(hollow_square(5))