def build_row_string(length):
    return "*" * length

def build_grid(dim):
    row_text = build_row_string(dim)
    return [row_text for _ in range(dim)]

if __name__ == '__main__':
    SIZE = 8
    grid = build_grid(SIZE)
    for line in grid:
        print(line)