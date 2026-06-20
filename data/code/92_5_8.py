class TruthFlipper:
    TRUE = True
    FALSE = False

    @staticmethod
    def flip_truth(iterable):
        for value in iterable:
            yield not value

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    flipped_values = list(TruthFlipper.flip_truth(sample_values))
    print(flipped_values)