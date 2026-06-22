def generate_right_aligned_triangle(size: int) -> str:
    lines = []
    for i in range(1, size + 1):
        current_line = ''.join(chr(ord('A') + j) for j in range(i))
        padded_line = current_line.rjust(size)
        lines.append(padded_line)
    return '\n'.join(lines)

if __name__ == '__main__':
    sample_size = 5
    result = generate_right_aligned_triangle(sample_size)
    print(result)