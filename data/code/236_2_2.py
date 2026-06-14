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
    sample_pattern = "###\n###\n###"
    repeat_count = 3
    repeated_output = generator.repeat_pattern(sample_pattern, repeat_count)
    print("--- Repeated Pattern ---")
    print(repeated_output)