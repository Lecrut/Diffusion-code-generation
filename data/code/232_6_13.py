class GrowingSequence:
    def generate_sequence(self, start, length):
        return list(map(lambda x: start + (x * 10), range(length)))

if __name__ == '__main__':
    sequence_generator = GrowingSequence()
    initial_term = 100
    sequence_length = 15
    generated_sequence = sequence_generator.generate_sequence(initial_term, sequence_length)
    print(generated_sequence)