def create_diamond(height):
    lines = []
    middle_index = height // 2
    row_index = 0
    while row_index < height:
        distance_from_center = abs(middle_index - row_index)
        star_quantity = height - (distance_from_center * 2)
        space_quantity = distance_from_center
        current_line = (' ' * space_quantity) + ('*' * star_quantity)
        lines.append(current_line)
        row_index += 1
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_height = 7
    output_text = create_diamond(sample_height)
    print(output_text)