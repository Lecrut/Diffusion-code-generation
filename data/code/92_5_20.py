class OppositeTruthGenerator:
    @staticmethod
    def opposite_truth(iterable):
        for value in iterable:
            yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    generator = OppositeTruthGenerator()
    for result in generator.opposite_truth(sample_values):
        print(result)