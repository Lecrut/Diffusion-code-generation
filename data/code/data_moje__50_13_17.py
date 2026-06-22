def print_inverted_triangle(size: int) -> str:
    if size <= 0:
        return ""
    lines = []
    for i in range(size):
        stars = '*' * (size - i)
        lines.append(stars)
    return '\n'.join(lines)

if __name__ == '__main__':
    size = 5
    result = print_inverted_triangle(size)
    print(result)