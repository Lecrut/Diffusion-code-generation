def generate_downward_triangle(num_rows):
    rows = []
    for i in range(num_rows):
        spaces = ' ' * i
        stars = '*' * (2 * (num_rows - i) - 1)
        rows.append(spaces + stars)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_downward_triangle(9))