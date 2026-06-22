def generate_right_aligned_alphabet_triangle(height):
    result = []
    for i in range(1, height + 1):
        line = []
        for j in range(height - i):
            line.append(" ")
        for j in range(1, i + 1):
            line.append(chr(ord('A') + j - 1))
        result.append("".join(line))
    return "\n".join(result)

if __name__ == '__main__':
    sample_height = 5
    output = generate_right_aligned_alphabet_triangle(sample_height)
    print(output)