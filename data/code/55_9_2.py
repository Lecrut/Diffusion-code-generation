def generate_mirrored_alphabet_triangle(height):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for i in range(1, height + 1):
        current_letters = []
        for j in range(i):
            current_letters.append(alphabet[j])
        line_left = "".join(current_letters)
        line_right = "".join(reversed(current_letters))
        full_line = line_left + line_right[:-1]
        result.append(full_line)
    return result

if __name__ == '__main__':
    sample_height = 5
    output = generate_mirrored_alphabet_triangle(sample_height)
    print(output)