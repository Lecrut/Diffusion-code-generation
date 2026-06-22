def generate_symmetric_pyramid(levels=4):
    result = []
    for i in range(1, levels + 1):
        num_str = str(i)
        row_parts = []
        for j in range(1, i + 1):
            row_parts.append(num_str)
        line = ' '.join(row_parts)
        padding = ' ' * (levels - i)
        centered_line = padding + line + padding
        result.append(centered_line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_symmetric_pyramid(4))