def perimeter_generator(line_segments):
    for segment in line_segments:
        total_length = sum(segment)
        yield 2 * total_length

if __name__ == '__main__':
    sample_segments = [(6, 8), (10, 24), (15, 36)]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)