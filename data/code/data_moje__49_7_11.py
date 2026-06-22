def generate_square(size: int):
    return (
        "* " * size for _ in range(size)
    )

if __name__ == '__main__':
    size = 3
    rows = generate_square(size)
    for row in rows:
        print(row.rstrip())