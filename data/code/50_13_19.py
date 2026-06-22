def print_inverted_triangle(size: int) -> None:
    for i in range(size, 0, -1):
        print("*" * i)

if __name__ == "__main__":
    sample_size = 5
    print_inverted_triangle(sample_size)