def get_diamond_half_height():
    return 4

def generate_diamond_row(row_index, half_height):
    spaces_count = half_height - row_index - 1
    stars_count = 2 * row_index + 1
    return ' ' * spaces_count + '*' * stars_count

def print_diamond(half_height):
    result_lines = []
    for i in range(half_height):
        result_lines.append(generate_diamond_row(i, half_height))
    for i in range(half_height - 2, -1, -1):
        result_lines.append(generate_diamond_row(i, half_height))
    return '\n'.join(result_lines)

def main():
    height = get_diamond_half_height()
    diamond_text = print_diamond(height)
    print(diamond_text)

if __name__ == '__main__':
    main()