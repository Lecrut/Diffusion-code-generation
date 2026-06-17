class PatternGenerator:
    def display_repeating_pattern(self, size, character):
        for i in range(size):
            for j in range(size):
                if (i + j) % 2 == 0:
                    print(character, end="")
                else:
                    print(" ", end="")
            print()
if __name__ == '__main__':
    generator = PatternGenerator()
    generator.display_repeating_pattern(5, "#")
    print("\n" * 2)
    generator.display_repeating_pattern(7, "@")