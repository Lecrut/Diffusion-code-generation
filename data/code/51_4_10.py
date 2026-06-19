def perimeter_generator(line_segments):
    if not isinstance(line_segments, list):
        raise TypeError("Input must be a list of line segments.")
    
    for segment in line_segments:
        if not isinstance(segment, (list, tuple)) or len(segment) != 2:
            raise ValueError("Each segment must be a list or tuple with exactly two lengths.")
        
        length1, length2 = segment
        if not all(isinstance(x, (int, float)) and x >= 0 for x in (length1, length2)):
            raise ValueError("Segment lengths must be non-negative numbers.")
        
        yield 2 * (length1 + length2)

if __name__ == '__main__':
    sample_segments = [
        [3.5, 4.8],
        [7.2, 9.6],
        [5.0, 10.0]
    ]
    
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)