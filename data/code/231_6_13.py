class PatternGenerator:
    def __init__(self, pattern, separator):
        self.pattern = pattern
        self.separator = separator

    def generate_pattern(self, repeat_count):
        return (self.pattern + self.separator) * repeat_count

if __name__ == '__main__':
    generator = PatternGenerator('hello', ' ')
    result = generator.generate_pattern(10)
    print(result.strip())