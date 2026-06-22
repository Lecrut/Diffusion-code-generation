def generate_diamond(rows):
    if rows <= 0:
        return ""
    
    half = (rows + 1) // 2
    lines = []
    
    for i in range(1, half + 1):
        spaces = " " * (half - i)
        stars = "*" * (2 * i - 1)
        lines.append(spaces + stars)
    
    if rows % 2 == 1:
        lower_lines = lines[-2::-1]
    else:
        lower_lines = lines[::-1]
    
    result_lines = lines + lower_lines
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_rows = 5
    output = generate_diamond(sample_rows)
    print(output)