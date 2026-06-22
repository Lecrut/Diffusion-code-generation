def build_inverted_right_angled_triangle(size):
    if size <= 0:
        return ""
    lines = []
    for i in range(size, 0, -1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(build_inverted_right_angled_triangle(5))