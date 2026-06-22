def build_inverted_triangle(height: int) -> list:
    if height <= 0:
        return []
    result = []
    for row in range(height, 0, -1):
        result.append('* ' * row)
    return result

if __name__ == '__main__':
    sample_height = 5
    triangle = build_inverted_triangle(sample_height)
    for line in triangle:
        print(line)