def generate_pyramid():
    rows = []
    row_count = 8
    for i in range(1, row_count + 1):
        max_num = i
        numbers = list(range(1, max_num + 1))
        numbers.extend(range(max_num - 1, 0, -1))
        row_str = ' '.join(map(str, numbers))
        padding = ' ' * (row_count - i)
        rows.append(padding + row_str)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_pyramid())