def generate_star_triangle(rows: int) -> str:
    if rows < 0:
        raise ValueError("Row count must be non-negative")
    lines = []
    for i in range(1, rows + 1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_rows = 20
    result = generate_star_triangle(sample_rows)
    print(result)