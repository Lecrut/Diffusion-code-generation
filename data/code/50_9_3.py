def display_inverted_triangle(height=5):
    lines = []
    for i in range(height, 0, -1):
        lines.append('*' * i)
    return '\n'.join(lines)

if __name__ == '__main__':
    result = display_inverted_triangle(5)
    print(result)