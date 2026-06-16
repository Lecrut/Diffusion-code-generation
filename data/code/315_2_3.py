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
            base = 1
            pattern = [base] * length
            return pattern
        else:
            return []
if __name__ == '__main__':
    generator = PatternGenerator()
    print("Arithmetic Progression (length 5):")
    result_arithmetic = generator.generate("arithmetic", 5)
    print(result_arithmetic)
    print("\nRepetition Pattern (length 7):")
    result_repetition = generator.generate("repetition", 7)
    print(result_repetition)
    print("\nArithmetic Progression (length 10):")
    result_arithmetic_long = generator.generate("arithmetic", 10)
    print(result_arithmetic_long)
    print("\nRepetition Pattern (length 3):")
    result_repetition_short = generator.generate("repetition", 3)
    print(result_repetition_short)