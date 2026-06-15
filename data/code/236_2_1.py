class ShapeGenerator:
    def draw_pattern(self, pattern):
        print(pattern)
    def repeat_pattern(self, pattern, n):
        result = ""
        for _ in range(n):
            result += pattern + "\n"
        return result
if __name__ == '__main__':
    generator = ShapeGenerator()
    sample_pattern = "#"
    sample_repetitions = 3
    repeated_output = generator.repeat_pattern(sample_pattern, sample_repetitions)
    print("--- Repeated Pattern ---")
    print(repeated_output)