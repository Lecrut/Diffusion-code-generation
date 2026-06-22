def print_triangle(height: int) -> str:
    result = []
    row_index = 1
    while row_index <= height:
        stars = '*' * row_index
        result.append(stars)
        row_index += 1
    return '\n'.join(result)

if __name__ == '__main__':
    height = 5
    triangle = print_triangle(height)
    print(triangle)