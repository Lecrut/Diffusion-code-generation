class SequenceGenerator:
    def generate_doubling_sequence(self, start_value, length):
        sequence = []
        current_value = start_value
        for _ in range(length):
            sequence.append(current_value)
            current_value *= 2
        return sequence
if __name__ == '__main__':
    generator = SequenceGenerator()
    start = 3
    length = 5
    result = generator.generate_doubling_sequence(start, length)
    print(result)