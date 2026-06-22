def generate_star_grid(size=8):
    return ["*" * size for _ in range(size)]

if __name__ == "__main__":
    sample_grid = generate_star_grid(8)
    for row in sample_grid:
        print(row)