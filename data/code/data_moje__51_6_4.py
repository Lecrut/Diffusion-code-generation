def generate_number_pyramid(levels: int=4) -> str:
    lines = []
    current_number = 1
    for level in range(1, levels + 1):
        nodes_in_level = 2 ** (level - 1)
        numbers_in_level = []
        for _ in range(nodes_in_level):
            numbers_in_level.append(str(current_number))
            current_number += 1
        line_content = ' '.join(numbers_in_level)
        spaces_before = ' ' * ((2 ** (levels - 1) - nodes_in_level) * 2)
        lines.append(spaces_before + line_content)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_number_pyramid()
    print(result)