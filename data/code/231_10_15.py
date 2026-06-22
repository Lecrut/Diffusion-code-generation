class PatternGenerator:
    PATTERN = ['A', 'B', 'C']
    
    @staticmethod
    def generate_pattern(n):
        return [PatternGenerator.PATTERN[i % 3] for i in range(n)]

if __name__ == '__main__':
    generator = PatternGenerator()
    sample_output1 = generator.generate_pattern(10)
    sample_output2 = generator.generate_pattern(15)
    print(sample_output1)
    print(sample_output2)