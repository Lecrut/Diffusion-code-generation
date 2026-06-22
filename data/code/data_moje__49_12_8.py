def generate_star_grid(size: int = 8) -> str:
    row = "* " * size
    return "\n".join([row for _ in range(size)])

if __name__ == '__main__':
    print(generate_star_grid())
    print(generate_star_grid(5))