def perimeter_generator(line_segments):
    for segment in line_segments:
        yield (2 * sum(segment))
if __name__ == '__main__':
    sample_segments = [[3, 4], [5, 12], [7, 24]]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)