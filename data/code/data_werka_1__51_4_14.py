def perimeter_generator(line_segments):
    def validate_segment(segment):
        if not isinstance(segment, list) or len(segment) != 2:
            raise ValueError("Each segment must be a list of two numeric values.")
        if not all(isinstance(length, (int, float)) and length >= 0 for length in segment):
            raise ValueError("Segment lengths must be non-negative numbers.")

    for segment in line_segments:
        validate_segment(segment)
        yield sum(segment) * 2

if __name__ == '__main__':
    sample_segments = [
        [3, 4],
        [5, 12],
        [7, 24]
    ]
    try:
        for perimeter in perimeter_generator(sample_segments):
            print(perimeter)
    except ValueError as e:
        print(f"Error: {e}")