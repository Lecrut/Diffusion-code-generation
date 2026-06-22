def draw_inverted_triangle(height):
    result = []
    for i in range(height):
        stars = '*' * (height - i)
        result.append(stars)
    return '\n'.join(result)

if __name__ == '__main__':
    print(draw_inverted_triangle(5))