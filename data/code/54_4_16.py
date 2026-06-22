def build_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "#"
    top_row = "#" * size
    middle_row = "#" + " " * (size - 2) + "#"
    rows = [top_row]
    for _ in range(size - 2):
        rows.append(middle_row)
    rows.append(top_row)
    return "\n".join(rows)

if __name__ == '__main__':
    print(build_hollow_square(10))