def generate_star_grid(size: int = 8) -> str:
    row = "* " * size + "\n"
    return row * size

if __name__ == "__main__":
    print(generate_star_grid())
    print(generate_star_grid(5))