def generate_right_aligned_pyramid(rows=8, chunk_size=64):
    def build_pyramid_lines(n):
        lines = []
        for i in range(1, n + 1):
            line = ' ' * (n - i) + str(i) * i
            lines.append(line)
        return lines

    text = '\n'.join(build_pyramid_lines(rows)) + '\n'
    for i in range(0, len(text), chunk_size):
        yield text[i:i + chunk_size]

if __name__ == '__main__':
    chunks = list(generate_right_aligned_pyramid())
    print(''.join(chunks))