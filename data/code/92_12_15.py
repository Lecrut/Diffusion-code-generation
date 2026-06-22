class TruthValueProcessor:
    OPPOSITE_MAP = {True: False, False: True}

    @staticmethod
    def find_opposite_truth_value(value: bool) -> bool:
        if not isinstance(value, bool):
            raise ValueError("Input must be a boolean")
        return TruthValueProcessor.OPPOSITE_MAP[value]

if __name__ == '__main__':
    print(TruthValueProcessor.find_opposite_truth_value(True))
    print(TruthValueProcessor.find_opposite_truth_value(False))