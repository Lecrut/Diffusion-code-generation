def generate_diamond(n):
    rows = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        rows.append(spaces + stars.strip())
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        rows.append(spaces + stars.strip())
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_diamond(6))