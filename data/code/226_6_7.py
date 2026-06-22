class RepeatingSequenceGenerator:
    MAX_COUNT = 50

    @staticmethod
    def generate(sequence):
        count = 0
        while count < RepeatingSequenceGenerator.MAX_COUNT:
            for item in sequence:
                yield item
                count += 1
                if count >= RepeatingSequenceGenerator.MAX_COUNT:
                    return

if __name__ == '__main__':
    sample_sequence = [1, 2]
    generator = RepeatingSequenceGenerator.generate(sample_sequence)
    result = list(generator)
    print(result)