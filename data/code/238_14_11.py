def generate_box(rows, cols):
    box = []
    for _ in range(rows):
        row = ['@'] * cols
        box.append(''.join(row))
    return '\n'.join(box)

if __name__ == '__main__':
    rows = 3
    cols = 2
    result = generate_box(rows, cols)
    print(result)