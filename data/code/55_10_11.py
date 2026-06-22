def print_alphabet_triangle(height: int) -> None:
    for i in range(1, height + 1):
        row = [chr(64 + j) for j in range(1, i + 1)]
        print(" ".join(row))

if __name__ == "__main__":
    sample_height = 5
    print_alphabet_triangle(sample_height)