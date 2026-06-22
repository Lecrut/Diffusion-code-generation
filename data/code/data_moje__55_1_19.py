import string

def print_alphabet_triangle(height=5):
    lines = []
    alphabet = string.ascii_uppercase
    max_width = len(alphabet[min(height, len(alphabet)) - 1]) * 2 + 1 if height <= len(alphabet) else height * 2 + 1
    max_width = 2 * height + 1 if height <= len(alphabet) else 2 * len(alphabet) + 1
    for i in range(1, height + 1):
        letters = alphabet[:i]
        line_content = letters
        total_chars = len(line_content)
        padding = (max_width - total_chars) // 2
        line = ' ' * padding + line_content + ' ' * padding
        lines.append(line)
    result = '\n'.join(lines)
    print(result)
    return result
if __name__ == '__main__':
    print_alphabet_triangle(5)