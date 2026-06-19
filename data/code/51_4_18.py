def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment)
if __name__ == '__main__':
    sample_segments = [[3, 4, 5], [1, 2, 2, 1], [5, 12, 13]]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)