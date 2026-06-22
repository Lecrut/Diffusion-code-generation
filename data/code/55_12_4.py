def generate_alphabet_triangle(size):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lines = []
    for i in range(1, size + 1):
        segment = alphabet[:i]
        if i == 1:
            line = segment
        else:
            left_part = segment[:-1]
            right_part = segment[:-1][::-1]
            line = left_part + segment[-1] + right_part
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_alphabet_triangle(5)
    print(result)