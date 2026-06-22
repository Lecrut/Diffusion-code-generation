def generate_diamond(rows: int) -> str:
    half = (rows + 1) // 2
    upper_lines = []
    for i in range(1, half + 1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        upper_lines.append(spaces + stars)
    
    lower_lines = []
    for i in range(half - 1, 0, -1):
        spaces = ' ' * (half - i)
        stars = '*' * (2 * i - 1)
        lower_lines.append(spaces + stars)
    
    result_lines = upper_lines + lower_lines
    return '\n'.join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    print(generate_diamond(sample_rows))