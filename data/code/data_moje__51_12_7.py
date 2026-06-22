def generate_number_pyramid(size: int) -> list[str]:
    if size <= 0:
        return []
    max_width = size * 2 - 1
    lines = []
    for row_num in range(1, size + 1):
        numbers = [str(i) for i in range(1, row_num + 1)]
        mirrored = numbers[:-1][::-1]
        full_row = numbers + mirrored
        line_content = ' '.join(full_row)
        center_pos = (max_width - len(line_content)) // 2
        line_str = ' ' * center_pos + line_content
        lines.append(line_str)
    return lines

if __name__ == '__main__':
    fixed_size = 6
    result = generate_number_pyramid(fixed_size)
    print('\n'.join(result))