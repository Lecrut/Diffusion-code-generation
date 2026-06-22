STAR_CHAR = '*'
DEFAULT_HEIGHT = 7

def build_triangle_lines(height):
    lines = []
    current_index = 1
    while current_index <= height:
        line_content = STAR_CHAR * current_index
        lines.append(line_content)
        current_index += 1
    return lines

def print_triangle_from_lines(lines):
    for line_content in lines:
        print(line_content)

def create_and_print_triangle(height):
    if height <= 0:
        return []
    generated_lines = build_triangle_lines(height)
    print_triangle_from_lines(generated_lines)
    return generated_lines

if __name__ == '__main__':
    test_height = 6
    output_list = create_and_print_triangle(test_height)
    print(output_list)