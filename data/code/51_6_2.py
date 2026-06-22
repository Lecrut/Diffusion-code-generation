def generate_binary_tree_pyramid():
    lines = []
    levels = 4
    max_width = 2 ** levels - 1
    for i in range(1, levels + 1):
        row_num = 2 ** i - 1
        row_str = str(row_num)
        padding = (max_width - len(row_str)) // 2
        line = ' ' * padding + row_str
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_binary_tree_pyramid()
    print(result)