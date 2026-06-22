class LucasSequenceGenerator:
    def generate(self, n):
        sequence = [2, 1]
        if n <= 2:
            return sequence[:n]
        for i in range(2, n):
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)
        return sequence

if __name__ == '__main__':
    generator = LucasSequenceGenerator()
    lucas_sequence = generator.generate(9)
    print(*lucas_sequence)