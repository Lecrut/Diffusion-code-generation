def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "#"
    
    row_top = "#" * n
    middle_row = "#" + " " * (n - 2) + "#"
    
    rows = []
    rows.append(row_top)
    if n > 2:
        rows.extend([middle_row] * (n - 2))
    rows.append(row_top)
    
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))
    print()
    print(generate_hollow_square(1))
    print()
    print(generate_hollow_square(8))