def generate_triangle():
    lines = []
    for row in range(1, 10):
        chars = []
        current_val = 65
        for _ in range(row):
            chars.append(chr(current_val))
            current_val += 1
        lines.append("".join(chars))
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_triangle())