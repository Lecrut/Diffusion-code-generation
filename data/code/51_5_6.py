def calculate_perimeters(segments):
    for segment in segments:
        perimeter = 2 * (segment[0] + segment[1])
        yield perimeter
if __name__ == '__main__':
    sample_segments = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    results = list(calculate_perimeters(sample_segments))
    print(results)