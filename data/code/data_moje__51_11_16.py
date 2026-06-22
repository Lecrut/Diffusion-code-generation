def build_pyramid(height):
    result = []
    for i in range(height):
        spaces = ' ' * (height - 1 - i)
        stars = '*' * (2 * i + 1)
        result.append(spaces + stars)
    return '\n'.join(result)

if __name__ == '__main__':
    sample_height = 7
    print(build_pyramid(sample_height))