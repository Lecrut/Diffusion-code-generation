def generate_right_aligned_pyramid():
    def chunk_generator(rows=8):
        for i in range(1, rows + 1):
            nums = ' '.join(str(j) for j in range(1, i + 1))
            padding = ' ' * ((rows - i) * 2 + (rows - 1))
            yield padding + nums
    return chunk_generator

if __name__ == '__main__':
    pyramid_chunks = list(generate_right_aligned_pyramid())
    for chunk in pyramid_chunks:
        print(chunk)