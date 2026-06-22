def validate_line_segment(segment):
    if not isinstance(segment, list) or len(segment) != 2:
        raise ValueError("Each segment must be a list of two numeric values.")
    if not all(isinstance(length, (int, float)) for length in segment):
        raise ValueError("Segment lengths must be numbers.")

def perimeter_generator(line_segments):
    for segment in line_segments:
        validate_line_segment(segment)
        yield sum(segment) * 2

if __name__ == '__main__':
    sample_segments = [
        [3.5, 4.5],
        [6.0, 13.0],
        [8.2, 25.1]
    ]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)