class DoublingSequenceGenerator:
    @staticmethod
    def generate_sequence(num_terms):
        return [2**i for i in range(1, num_terms + 1)]

if __name__ == '__main__':
    sample_value = 5
    result = DoublingSequenceGenerator.generate_sequence(sample_value)
    print(result)