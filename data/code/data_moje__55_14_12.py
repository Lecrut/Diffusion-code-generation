def generate_centered_alphabet_triangle(height: int) -> list:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if height > len(alphabet):
        height = len(alphabet)
    result = []
    for i in range(height):
        segment = alphabet[: i + 1]
        reversed_segment = segment[-2::-1] if i > 0 else ""
        full_row = segment + reversed_segment
        padding = " " * (height - i - 1)
        result.append(padding + full_row + padding)
    return result

if __name__ == '__main__':
    sample_height = 5
    printed_lines = generate_centered_alphabet_triangle(sample_height)
    for line in printed_lines:
        print(line)