def diamond_pattern(radius):
    result = []
    for i in range(-radius, radius + 1):
        spaces = ' ' * abs(i)
        stars = '*' * (2 * (radius - abs(i)) + 1)
        result.append(spaces + stars)
    return '\n'.join(result)

if __name__ == '__main__':
    print(diamond_pattern(3))