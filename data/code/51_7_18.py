def generate_right_aligned_number_pyramid(rows):
    def chunk_generator(r):
        lines = []
        for i in range(1, r + 1):
            row_numbers = [str(j) for j in range(1, i + 1)]
            line_content = " ".join(row_numbers)
            padding = r - i
            line = " " * padding + line_content
            lines.append(line)
        for line in lines:
            yield line

    return chunk_generator(rows)

if __name__ == '__main__':
    rows = 8
    generator = generate_right_aligned_number_pyramid(rows)
    print('\n'.join(generator))