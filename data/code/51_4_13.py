def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment) * 2

if __name__ == '__main__':
    sample_segments = [
        {'type': 'rect', 'lengths': [3, 4]},
        {'type': 'rect', 'lengths': [5, 12]},
        {'type': 'rect', 'lengths': [7, 24]}
    ]
    for segment in sample_segments:
        perimeter = next(perimeter_generator([segment['lengths']]))
        print(perimeter)