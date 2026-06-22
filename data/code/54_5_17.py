def generate_hollow_square(size, char='*'):
    if size <= 0:
        return ""
    if size == 1:
        return char
    middle_row = char + (size - 2) * ' ' + char
    top_bottom = char * size
    rows = [top_bottom] + [middle_row] * (size - 2) + [top_bottom]
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))