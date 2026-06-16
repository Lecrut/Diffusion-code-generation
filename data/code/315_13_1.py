class PatternGenerator:
    def display_repeating_pattern(self, size, character):
        for i in range(size):
            line = ""
            for j in range(size):
                if (i + j) % 2 == 0:
                    line += character
                else:
                    line += " "
            print(line)
if __name__ == '__main__':
    generator = PatternGenerator()
    generator.display_repeating_pattern(5, '*')
    print("\n")
    generator.display_repeating_pattern(7, '#')