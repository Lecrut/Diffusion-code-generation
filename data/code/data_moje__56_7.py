def format_multiplication_table(base, rows=10, cols=10):
    if base < 0:
        return "Error: Base must be non-negative."
    if rows < 1 or cols < 1:
        return "Error: Rows and cols must be positive."
    
    width = len(str(base * cols)) + 1
    if width < 1:
        width = 1
    
    lines = []
    for i in range(1, rows + 1):
        row_values = []
        for j in range(1, cols + 1):
            product = base * j
            row_values.append(f"{product:>{width}}")
        lines.append(f"{i * base:>{width}} | {' '.join(row_values)}")
    
    separator = "+" + "-" * (width + 2) * (cols + 1)
    header = f"{'X':>{width}} | {' '.join(str(j).rjust(width) for j in range(1, cols + 1))}"
    
    result = f"{header}\n{separator}\n" + "\n".join(lines)
    return result

if __name__ == '__main__':
    print(format_multiplication_table(5, 10, 10))