class SegmentPerimeterCalculator:
    @staticmethod
    def calculate_perimeter(segment):
        return sum(segment) * 2

    @classmethod
    def perimeter_generator(cls, line_segments):
        for segment in line_segments:
            yield cls.calculate_perimeter(segment)

if __name__ == '__main__':
    sample_segments = [
        [3, 4],
        [5, 12],
        [7, 24]
    ]
    calculator = SegmentPerimeterCalculator()
    for perimeter in calculator.perimeter_generator(sample_segments):
        print(perimeter)