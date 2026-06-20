class TruthFlipper:
    TRUE = True
    FALSE = False

    @staticmethod
    def flip_value(value):
        return not value

    @staticmethod
    def opposite_truth_values(iterable):
        for value in iterable:
            yield TruthFlipper.flip_value(value)

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    flipped_values = list(TruthFlipper.opposite_truth_values(sample_values))
    print(flipped_values)