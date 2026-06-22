def generate_star_grid(size: int = 8) -> str:
    row = "* " * size
    rows = [row for _ in range(size)]
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_star_grid(8))