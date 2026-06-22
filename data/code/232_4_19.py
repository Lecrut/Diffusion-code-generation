class GrowingNumbersGenerator:
    START = 1

    @staticmethod
    def generate(N):
        return list(range(GrowingNumbersGenerator.START, N + 1))

if __name__ == '__main__':
    sample_value = 50
    generator = GrowingNumbersGenerator()
    result = generator.generate(sample_value)
    print(result)