class DoublingSequenceGenerator:
    @staticmethod
    def generate(num_terms):
        sequence = []
        current_value = 1
        for _ in range(num_terms):
            sequence.append(current_value)
            current_value *= 2
        return sequence

if __name__ == '__main__':
    sample_value = 5
    result = DoublingSequenceGenerator.generate(sample_value)
    print(result)