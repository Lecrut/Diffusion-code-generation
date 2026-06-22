class LineSegment:
    def __init__(self, lengths):
        self.lengths = lengths

    @staticmethod
    def calculate_perimeter(lengths):
        return sum(lengths) * 2

def perimeter_generator(line_segments):
    for segment in line_segments:
        yield LineSegment.calculate_perimeter(segment.lengths)

if __name__ == '__main__':
    sample_segments = [
        LineSegment([3, 4]),
        LineSegment([5, 12]),
        LineSegment([7, 24])
    ]
    for perimeter in perimeter_generator(sample_segments):
        print(perimeter)