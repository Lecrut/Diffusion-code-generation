def generate_hollow_square(size, char):
    if size <= 0:
        return ""
    if size == 1:
        return char
    row = char * size
    inner_row = char + ' ' * (size - 2) + char
    rows = [row] + [inner_row] * (size - 2) + [row]
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5, '*'))