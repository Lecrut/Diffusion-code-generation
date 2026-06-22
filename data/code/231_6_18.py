class PatternGenerator:
    REPEAT_COUNT = 10
    SEPARATOR = ' '

    @staticmethod
    def generate_pattern():
        return (PatternGenerator.SEPARATOR.join(['hello'] * PatternGenerator.REPEAT_COUNT)).strip()

if __name__ == '__main__':
    result = PatternGenerator.generate_pattern()
    print(result)