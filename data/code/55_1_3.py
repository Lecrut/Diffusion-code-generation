def get_centered_alphabet_triangle(height):
    if height <= 0:
        return ""
    
    lines = []
    for i in range(1, height + 1):
        row_char = chr(ord('A') + i - 1)
        row_content = (row_char + " ") * i
        row_content = row_content.rstrip()
        width = (height * 2) - 1
        padding = (width - len(row_content)) // 2
        line = " " * padding + row_content
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    result = get_centered_alphabet_triangle(sample_height)
    print(result)