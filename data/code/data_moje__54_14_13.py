def render_hollow_square(size, char='*'):
    if size < 1:
        return ''
    if size == 1:
        return char
    top_bottom = char * size
    middle = char + ' ' * (size - 2) + char
    lines = [top_bottom]
    if size > 2:
        lines.extend([middle] * (size - 2))
        lines.append(top_bottom)
    else:
        lines.append(top_bottom)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(render_hollow_square(5))