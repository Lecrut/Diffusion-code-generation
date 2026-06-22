class NumberSequenceGenerator:
    def generate_sequence(self, n):
        return ','.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    generator = NumberSequenceGenerator()
    N = 5
    sequence = generator.generate_sequence(N)
    print(sequence)