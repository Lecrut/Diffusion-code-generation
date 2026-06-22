def generate_star_grid(size=8):
    if size <= 0:
        return []
    line = "* " * size
    return [line for _ in range(size)]

if __name__ == "__main__":
    grid = generate_star_grid(5)
    for row in grid:
        print(row)