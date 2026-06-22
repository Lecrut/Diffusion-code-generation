def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment) * 2

if __name__ == '__main__':
    SAMPLE_SEGMENTS = [
        [3, 4],
        [5, 12],
        [7, 24]
    ]
    for perimeter in perimeter_generator(SAMPLE_SEGMENTS):
        print(perimeter)