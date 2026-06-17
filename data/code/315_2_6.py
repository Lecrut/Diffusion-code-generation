class PatternGenerator:
    def generate(self, pattern_type, length):
        if pattern_type == "arithmetic":
            if length <= 0:
                return []
            start = 1
            diff = 1
            pattern = [start]
            for _ in range(1, length):
                next_val = pattern[-1] + diff
                pattern.append(next_val)
            return pattern
        elif pattern_type == "repetition":
            if length <= 0:
                return []
            base = 5
            pattern = [base] * length
            return pattern
        else:
            return []
if __name__ == '__main__':
    generator = PatternGenerator()
    print("Arithmetic Pattern (length 5):")
    print(generator.generate("arithmetic", 5))
    print("\nRepetition Pattern (length 7):")
    print(generator.generate("repetition", 7))
    print("\nArithmetic Pattern (length 10):")
    print(generator.generate("arithmetic", 10))
    print("\nRepetition Pattern (length 3):")
    print(generator.generate("repetition", 3))