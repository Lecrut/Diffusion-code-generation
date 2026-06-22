class EvenNumberGenerator:
    def generate_first_n_evens(self, n):
        return [2 * i for i in range(1, n + 1)]

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    sample_n = 10
    result = generator.generate_first_n_evens(sample_n)
    print(result)