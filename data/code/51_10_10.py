def generate_number_pyramid():
    height = 5
    max_width = len(str(height)) + 2 * (height - 1)
    for row in range(1, height + 1):
        numbers = [str(i) for i in range(1, row + 1)]
        row_str = " ".join(numbers)
        padding = (max_width - len(row_str)) // 2
        print(" " * padding + row_str)

if __name__ == "__main__":
    generate_number_pyramid()