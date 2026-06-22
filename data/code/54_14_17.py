HOLLOW_CHARS = {
    'corner': '*',
    'edge': '*',
    'fill': ' ',
    'join': '*'
}

CHAR_MAP = {
    'top_left': 'corner',
    'top_right': 'corner',
    'bottom_left': 'corner',
    'bottom_right': 'corner',
    'top_edge': 'edge',
    'bottom_edge': 'edge',
    'left_edge': 'edge',
    'right_edge': 'edge',
    'center': 'fill'
}

EDGE_OFFSETS = {
    'top': 0,
    'bottom': 1
}

EDGE_SIDE_OFFSETS = {
    'left': 0,
    'right': 1
}

def render_hollow_square(size):
    if size < 1:
        return ""
    if size == 1:
        return CHAR_MAP['center']
    result_lines = []
    width = size
    height = size
    for row in range(height):
        row_chars = []
        for col in range(width):
            if row in (0, height - 1):
                char_key = 'edge'
            elif col in (0, width - 1):
                char_key = 'edge'
            else:
                char_key = 'fill'
            row_chars.append(HOLLOW_CHARS[char_key])
        result_lines.append("".join(row_chars))
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_size = 6
    print(render_hollow_square(sample_size))