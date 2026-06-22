def build_hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    edge_row = '*' * size
    inner_row = '*' + ' ' * (size - 2) + '*' if size > 2 else '*'
    rows = [edge_row]
    for _ in range(size - 2):
        rows.append(inner_row)
    if size > 1:
        rows.append(edge_row)
    return '\n'.join(rows)

if __name__ == '__main__':
    result = build_hollow_square(10)
    print(result)