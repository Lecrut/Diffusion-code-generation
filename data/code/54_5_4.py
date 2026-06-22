def generate_hollow_square(size: int, char: str = '#') -> str:
    if size <= 0:
        return ""
    if size == 1:
        return char
    row = char * size
    inner = row[0] + (' ' * (size - 2)) + row[-1]
    rows = [row] + [inner] * (size - 2) + [row]
    return '\n'.join(rows)

if __name__ == '__main__':
    result = generate_hollow_square(5, '#')
    print(result)