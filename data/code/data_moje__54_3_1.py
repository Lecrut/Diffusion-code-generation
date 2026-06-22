def generate_hollow_square(n: int, char: str='#') -> str:
    if n <= 0:
        return ''
    if n == 1:
        return char
    top_bottom_row = char * n
    middle_row = char + (n - 2) * ' ' + char
    lines = []
    lines.append(top_bottom_row)
    for _ in range(n - 2):
        lines.append(middle_row)
    lines.append(top_bottom_row)
    return '\n'.join(lines)
if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)
    result2 = generate_hollow_square(3, char='*')
    print(result2)
    result3 = generate_hollow_square(1, char='X')
    print(result3)
    result4 = generate_hollow_square(0)
    print(repr(result4))