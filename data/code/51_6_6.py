def generate_pyramid(levels: int) -> list[str]:
    result = []
    for level in range(1, levels + 1):
        numbers = [str(2 ** (level - 1 - i)) for i in range(level)]
        row_str = ' '.join(numbers)
        result.append(row_str)
    return result

if __name__ == '__main__':
    pyramid_levels = 4
    output = generate_pyramid(pyramid_levels)
    for line in output:
        print(line)