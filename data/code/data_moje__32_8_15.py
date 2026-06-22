class RectangleCalculator:
    def __init__(self):
        self._multiplier_cache = {}

    def calculate_area(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        return float(width) * float(height)

def run_computation_loop(rec_calculator, iterations):
    total_area = 0.0
    width_sequence = [10.5, 20.0, 15.75, 30.2]
    height_sequence = [5.0, 8.5, 12.0, 6.25]
    for i in range(iterations):
        w = width_sequence[i % len(width_sequence)]
        h = height_sequence[i % len(height_sequence)]
        area = rec_calculator.calculate_area(w, h)
        total_area += area
    return total_area

if __name__ == '__main__':
    calculator = RectangleCalculator()
    single_width = 7.5
    single_height = 4.2
    single_result = calculator.calculate_area(single_width, single_height)
    print(single_result)
    loop_iterations = 100
    loop_total = run_computation_loop(calculator, loop_iterations)
    print(loop_total)