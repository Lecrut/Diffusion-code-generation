def generate_diamond_pattern(height):
    if height <= 0:
        return ""
    half = (height + 1) // 2
    lines = []
    for i in range(1, half + 1):
        spaces = " " * (half - i)
        chars = ""
        for j in range(i):
            char_code = ord('A') + j
            if j > 0:
                chars += chr(char_code)
                if j < i - 1:
                    chars += chr(char_code - 1) + " "
                else:
                    chars += chr(char_code - 1) if j == i - 1 else ""
            else:
                chars = chr(char_code)
                if i > 1:
                    chars += " " * (2 * (i - 1) - 1) + chr(char_code)
        line = spaces + chars
        lines.append(line)
    for i in range(half - 1, 0, -1):
        spaces = " " * (half - i)
        chars = ""
        for j in range(i):
            char_code = ord('A') + j
            if j > 0:
                chars += chr(char_code)
                if j < i - 1:
                    chars += chr(char_code - 1) + " "
                else:
                    chars += chr(char_code - 1) if j == i - 1 else ""
            else:
                chars = chr(char_code)
                if i > 1:
                    chars += " " * (2 * (i - 1) - 1) + chr(char_code)
        line = spaces + chars
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    sample_height = 5
    print(generate_diamond_pattern(sample_height))