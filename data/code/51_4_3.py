def perimeter_generator(line_segments):
    for segment in line_segments:
        yield sum(segment) * 2

if __name__ == '__main__':
    sample_segments = [
        {'length1': 3, 'length2': 4},
        {'length1': 5, 'length2': 12},
        {'length1': 7, 'length2': 24}
    ]
    for segment in sample_segments:
        lengths = [segment['length1'], segment['length2']]
        perimeter = next(perimeter_generator([lengths]))
        print(perimeter)