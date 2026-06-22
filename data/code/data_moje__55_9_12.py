def generate_mirrored_alphabet_triangle(height: int = 5) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    for i in range(height):
        left_part = alphabet[:i + 1]
        right_part = alphabet[i::-1]
        line = left_part + right_part
        lines.append(line)
    
    max_width = len(lines[-1])
    result_lines = []
    for line in lines:
        mirrored = line[::-1]
        full_line = line + mirrored
        result_lines.append(full_line)
    
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(generate_mirrored_alphabet_triangle())