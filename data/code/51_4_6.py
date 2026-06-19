class LineSegment:
    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def perimeter(self):
        return 2 * (self.length1 + self.length2)

def perimeter_generator(line_segments):
    for segment in line_segments:
        yield segment.perimeter()

if __name__ == '__main__':
    sample_segments = [
        LineSegment(3, 4),
        LineSegment(5, 12),
        LineSegment(7, 24)
    ]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)