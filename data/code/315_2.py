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
    print("Arithmetic Progression (length 5):", generator.generate("arithmetic", 5))
    print("Repetition (length 7):", generator.generate("repetition", 7))
    print("Arithmetic Progression (length 0):", generator.generate("arithmetic", 0))
    print("Repetition (length -2):", generator.generate("repetition", -2))