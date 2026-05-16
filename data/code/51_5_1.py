def calculate_perimeters(line_segments):
    for segment in line_segments:
        perimeter = segment[0] + segment[1]
        yield perimeter
if __name__ == '__main__':
    segments = [
        (3, 4),
        (5, 12),
        (10, 20)
    ]
    results = list(calculate_perimeters(segments))
    print(results)