class RepeatingSequenceGenerator:
    def __init__(self, sequence):
        self.sequence = sequence

    def repeat(self):
        count = 0
        while True:
            for item in self.sequence:
                yield item
                count += 1
                if count >= 50:
                    return

if __name__ == '__main__':
    sample_sequence = [1, 2]
    generator_instance = RepeatingSequenceGenerator(sample_sequence)
    result = [next(generator_instance.repeat()) for _ in range(50)]
    print(result)