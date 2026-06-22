def generate_right_aligned_pyramid():
    rows = []
    for i in range(1, 9):
        line = ' '.join(str(j) for j in range(1, i + 1))
        rows.append(line)
    max_len = max(len(r) for r in rows)
    for r in rows:
        yield r.rjust(max_len)

if __name__ == '__main__':
    for chunk in generate_right_aligned_pyramid():
        print(chunk)