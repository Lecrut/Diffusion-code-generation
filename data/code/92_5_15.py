class TruthFlipper:
    @staticmethod
    def flip_truth_value(value):
        return not value

    def flip_values(self, iterable):
        for value in iterable:
            yield self.flip_truth_value(value)

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    flipper = TruthFlipper()
    flipped_values = list(flipper.flip_values(sample_values))
    print(flipped_values)