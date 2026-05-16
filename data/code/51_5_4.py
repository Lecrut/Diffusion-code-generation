def calculate_perimeters(segments):
    for segment in segments:
        perimeter = 2 * (segment['length'] + segment['width'])
        yield perimeter
if __name__ == '__main__':
    sample_segments = [
        {'length': 10, 'width': 5},
        {'length': 20, 'width': 3},
        {'length': 7, 'width': 12}
    ]
    results = list(calculate_perimeters(sample_segments))
    for result in results:
        print(result)