def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    rows = [top_bottom]
    for _ in range(size - 2):
        rows.append(middle)
    rows.append(top_bottom)
    return "\n".join(rows)

if __name__ == '__main__':
    sample_sizes = [3, 5, 1]
    for s in sample_sizes:
        print(f"Size {s}:")
        print(generate_hollow_square(s))
        print("-" * 10)