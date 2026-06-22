def render_downward_stars(count):
    if count <= 0:
        return ""
    lines = []
    for step in range(1, count + 1):
        length = count - step + 1
        lines.append('*' * length)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_rows = 9
    rendered = render_downward_stars(sample_rows)
    print(rendered)