def print_square_of_stars(size: int) -> str:
    return ("\n").join("*" * size for _ in range(size))

if __name__ == "__main__":
    print(print_square_of_stars(6))