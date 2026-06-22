def perimeter_generator(line_segments):
    for segment in line_segments:
        yield (2 * sum(segment))
if __name__ == '__main__':
    sample_line_segments = [[3, 4], [5, 5], [7, 8, 9]]
    for perimeter in perimeter_generator(sample_line_segments):
        print(perimeter)