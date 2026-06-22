def print_alphabet_triangle(rows: int) -> None:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(rows):
        line = " " * (rows - i - 1) + alphabet[:i + 1] + " " * (rows - i - 1)
        print(line)

if __name__ == '__main__':
    sample_rows = 5
    print_alphabet_triangle(sample_rows)