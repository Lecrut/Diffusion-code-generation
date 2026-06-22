import string

def print_centered_alphabet_triangle(height):
    if height <= 0:
        return ""
    
    alphabet = string.ascii_uppercase
    if height > len(alphabet):
        alphabet = alphabet + alphabet.upper()
    
    lines = []
    max_width = 2 * height - 1
    
    for i in range(height):
        current_char = alphabet[i]
        num_chars = 2 * i + 1
        char_line = current_char * num_chars
        padding = (max_width - num_chars) // 2
        line = ' ' * padding + char_line + ' ' * padding
        lines.append(line)
    
    return '\n'.join(lines)

if __name__ == '__main__':
    result = print_centered_alphabet_triangle(5)
    print(result)