def make_hollow_square(size):
    if size <= 0:
        return []
    row_str = '#' * size
    rows = [row_str]
    inner = '#' + ' ' * (size - 2) + '#' if size > 2 else '#'
    for _ in range(size - 2):
        rows.append(inner)
    rows.append(row_str)
    return rows

if __name__ == '__main__':
    result = make_hollow_square(10)
    for row in result:
        print(row)