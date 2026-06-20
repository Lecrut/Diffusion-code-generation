def find_opposite_truth_value(value: bool) -> bool:
    return value ^ 1

if __name__ == '__main__':
    negator = TruthValueNegator()
    print(negator.find_opposite_truth_value(True))
    print(negator.find_opposite_truth_value(False))

class TruthValueNegator:
    @staticmethod
    def find_opposite_truth_value(value: bool) -> bool:
        return value ^ 1