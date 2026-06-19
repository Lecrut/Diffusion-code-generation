def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment)
if __name__ == '__main__':
    sample_line_segments = [[3, 4, 5], [1, 2, 3, 4], [5, 5, 5, 5, 5]]
    for perimeter in perimeter_generator(sample_line_segments):
        print(perimeter)