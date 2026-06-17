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
            base_pattern = [1, 2]
            if not base_pattern:
                return []
            base_len = len(base_pattern)
            full_pattern = []
            for i in range(length):
                index = i % base_len
                full_pattern.append(base_pattern[index])
            return full_pattern
        else:
            return []
if __name__ == '__main__':
    generator = PatternGenerator()
    print("Arithmetic Pattern (length 5):", generator.generate("arithmetic", 5))
    print("Repetition Pattern (length 8):", generator.generate("repetition", 8))
    print("Arithmetic Pattern (length 0):", generator.generate("arithmetic", 0))
    print("Repetition Pattern (length 1):", generator.generate("repetition", 1))
    print("Unknown Pattern Type:", generator.generate("unknown", 5))