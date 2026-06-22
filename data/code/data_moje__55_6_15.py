def hollow_alphabet_triangle(base_width):
    if base_width < 1:
        return ""
    
    result = []
    current_char = 'A'
    
    for row in range(1, base_width + 1):
        line = []
        for col in range(1, row + 1):
            if col == 1 or col == row or row == base_width:
                line.append(current_char)
            else:
                line.append(' ')
            current_char = chr((ord(current_char) - ord('A') + 1) % 26 + ord('A'))
        result.append(''.join(line))
    
    return '\n'.join(result)

if __name__ == '__main__':
    sample_width = 5
    output = hollow_alphabet_triangle(sample_width)
    print(output)