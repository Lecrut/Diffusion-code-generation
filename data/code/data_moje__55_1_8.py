def print_centered_alphabet_triangle(height: int) -> str:
    if height < 1:
        return ""
    
    lines = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in range(height):
        char = alphabet[i % 26]
        spaces = " " * (height - 1 - i)
        line = spaces + char + spaces
        lines.append(line)
    
    return "\n".join(lines)

if __name__ == "__main__":
    sample_height = 5
    result = print_centered_alphabet_triangle(sample_height)
    print(result)