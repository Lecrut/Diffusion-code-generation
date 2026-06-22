class PatternGenerator:
    PATTERN = ['A', 'B', 'C']
    
    @staticmethod
    def generate_pattern(n):
        return [PatternGenerator.PATTERN[i % 3] for i in range(n)]

if __name__ == '__main__':
    generator_instance = PatternGenerator()
    sample_output_1 = generator_instance.generate_pattern(10)
    print(sample_output_1)

    sample_output_2 = generator_instance.generate_pattern(15)
    print(sample_output_2)