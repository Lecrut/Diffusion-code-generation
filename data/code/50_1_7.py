def generate_isosceles_triangle(height):
    pattern = []
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        pattern.append(spaces + stars)
    return "\n".join(pattern)

if __name__ == '__main__':
    print(generate_isosceles_triangle(7))