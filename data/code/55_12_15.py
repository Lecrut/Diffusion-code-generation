def generate_alphabet_triangle(size):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if size < 1:
        return []
    
    lines = []
    for i in range(size):
        repeat_count = i + 1
        char_index = i % 26
        char = alphabet[char_index]
        row = (char * repeat_count).rjust(size * 2 - 1)
        lines.append(row)
    
    return lines

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    for line in result:
        print(line)