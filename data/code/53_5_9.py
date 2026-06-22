def print_reverse_number_triangle(rows=5):
    for i in range(1, rows + 1):
        digits = list(range(1, i + 1))
        reversed_digits = digits[::-1]
        combined = digits + reversed_digits[1:]
        print(" ".join(map(str, combined)))

if __name__ == "__main__":
    print_reverse_number_triangle(5)