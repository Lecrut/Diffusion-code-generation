class PatternGenerator:
    CHARACTERS = 'abcde'
    
    @staticmethod
    def generate_pattern(length):
        return (PatternGenerator.CHARACTERS * ((length // len(PatternGenerator.CHARACTERS)) + 1))[:length]

if __name__ == '__main__':
    pattern = PatternGenerator.generate_pattern(50)
    print(pattern)