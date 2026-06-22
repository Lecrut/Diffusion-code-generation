class PatternRepeater:
    def repeat_pattern(self, pattern, n):
        return [item for sublist in [[pattern] * n for _ in range(n)] for item in sublist]

if __name__ == '__main__':
    repeater = PatternRepeater()
    sample_pattern = "###\n###\n###"
    repeat_count = 3
    repeated_output = repeater.repeat_pattern(sample_pattern, repeat_count)
    print("--- Repeated Pattern ---")
    for line in repeated_output:
        print(line)