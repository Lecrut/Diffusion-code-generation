def calculate_area(base, height):
    return 0.5 * base * height

class TriangleAreaCalculator:
    def __init__(self, input_data):
        self.input_data = input_data
        self.results = []

    def process(self):
        for entry in self.input_data:
            base, height = entry
            area = calculate_area(base, height)
            self.results.append(area)

if __name__ == '__main__':
    sample_input = [
        (3, 4),
        (5, 12),
        (7, 24),
        (9, 16)
    ]
    
    calculator = TriangleAreaCalculator(sample_input)
    calculator.process()
    print(calculator.results)