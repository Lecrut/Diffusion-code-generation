def print_centered_number_pyramid(rows):
    max_width = (rows - 1) * 2 + 1
    lines = [
        f"{''.join(str(n) for n in range(1, i + 1)) + ''.join(str(n) for n in range(i - 1, 0, -1)):^{max_width}}"
        for i in range(1, rows + 1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_rows = 7
    print(print_centered_number_pyramid(sample_rows))