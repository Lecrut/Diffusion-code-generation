def create_diamond(n: int) -> str:
    lines = []
    upper = list(range(1, n))
    lower = list(range(n, 0, -1))
    rows = upper + lower

    for count in rows:
        spaces = ' ' * (n - count)
        stars = '* ' * count
        lines.append(f"{spaces}{stars.rstrip()}")

    middle_stars = '* ' * n
    middle_line = f"{' ' * 0}{middle_stars.rstrip()}"
    lines.insert(n - 1, middle_line)

    return '\n'.join(lines)

if __name__ == '__main__':
    n = 5
    print(create_diamond(n))