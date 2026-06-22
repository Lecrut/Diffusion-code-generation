def generate_right_aligned_reverse_triangle(rows):
    result = []
    for i in range(rows, 0, -1):
        line_numbers = [str(j) for j in range(i, 0, -1)]
        line = " ".join(line_numbers)
        padded_line = line.rjust(2 * rows)
        result.append(padded_line)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_right_aligned_reverse_triangle(4))