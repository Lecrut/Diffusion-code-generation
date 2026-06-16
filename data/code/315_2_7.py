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
    print("Arithmetic Progression (start=1, diff=1, length=5):")
    result_arithmetic = generator.generate("arithmetic", 5)
    print(result_arithmetic)
    print("\nRepetition (base=1, length=6):")
    result_repetition = generator.generate("repetition", 6)
    print(result_repetition)
    print("\nArithmetic Progression (start=5, diff=3, length=4):")
    result_arithmetic_custom = generator.generate("arithmetic", 4)
    print(result_arithmetic_custom)
    print("\nRepetition (base=10, length=3):")
    result_repetition_custom = generator.generate("repetition", 3)
    print(result_repetition_custom)