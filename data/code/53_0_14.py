def generate_reverse_triangle(rows=5):
    lines = ["".join(str(rows - r + 1 - i) for i in range(rows - r + 1)) for r in range(1, rows + 1)]
    max_len = max(len(line) for line in lines) if lines else 0
    return "\n".join(line.rjust(max_len) for line in lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    print(result)