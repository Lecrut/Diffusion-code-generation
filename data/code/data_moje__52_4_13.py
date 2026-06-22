def generate_diamond(width: int) -> list[str]:
    half = width // 2
    rows = []
    for i in range(-half, half + 1):
        star_count = width - 2 * abs(i)
        space_count = abs(i)
        row = ' ' * space_count + '*' * star_count
        rows.append(row)
    return rows

def print_diamond(rows: list[str]) -> None:
    for row in rows:
        print(row)

if __name__ == '__main__':
    width = 9
    diamond = generate_diamond(width)
    print_diamond(diamond)