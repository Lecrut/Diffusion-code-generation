def generate_mirrored_alphabet_triangle(height):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i in range(1, height + 1):
        chars = alphabet[:i]
        mirrored = chars + chars[-2::-1] if i > 1 else chars
        result.append(mirrored)
    return result

if __name__ == "__main__":
    sample_height = 5
    output_lines = generate_mirrored_alphabet_triangle(sample_height)
    for line in output_lines:
        print(line)