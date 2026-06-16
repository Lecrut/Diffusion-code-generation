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
            base_pattern = [1, 2, 3]
            if not base_pattern:
                return []
            cycle_len = len(base_pattern)
            result = []
            for i in range(length):
                result.append(base_pattern[i % cycle_len])
            return result
        else:
            return []
if __name__ == '__main__':
    generator = PatternGenerator()
    print("Arithmetic Progression (length 5):", generator.generate("arithmetic", 5))
    print("Repetition (length 8):", generator.generate("repetition", 8))
    print("Arithmetic Progression (length 0):", generator.generate("arithmetic", 0))
    print("Repetition (length 1):", generator.generate("repetition", 1))