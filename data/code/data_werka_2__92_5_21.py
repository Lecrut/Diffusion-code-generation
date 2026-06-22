class TruthFlipper:
    TRUE_MAP = {True: False}
    FALSE_MAP = {False: True}
    INVERSE_TABLE = {**TRUE_MAP, **FALSE_MAP}

    @staticmethod
    def _validate(item):
        if item not in TruthFlipper.INVERSE_TABLE:
            raise ValueError(f"Expected boolean, got {type(item).__name__}")
        return TruthFlipper.INVERSE_TABLE[item]

    @staticmethod
    def opposite_truth_values(iterable):
        for item in iterable:
            yield TruthFlipper._validate(item)

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    flipped_result = list(TruthFlipper.opposite_truth_values(sample_values))
    print(flipped_result)