BOX_PATTERN = {
    'top_bottom': lambda width: '*' * width,
    'middle': lambda width: '*' + ' ' * (width - 2) + '*'
}

def generate_box(width=5, height=3):
    box_parts = [BOX_PATTERN['top_bottom'](width)]
    for _ in range(height - 2):
        box_parts.append(BOX_PATTERN['middle'](width))
    box_parts.append(BOX_PATTERN['top_bottom'](width))
    return '\n'.join(box_parts)

if __name__ == '__main__':
    print(generate_box())