def calculate_perimeters(segments):
    for segment in segments:
        perimeter = segment[0] + segment[1]
        yield perimeter
if __name__ == '__main__':
    line_segments = [
        [3, 4],
        [5, 12],
        [1, 1],
        [6, 8]
    ]
    results = list(calculate_perimeters(line_segments))
    print(results)