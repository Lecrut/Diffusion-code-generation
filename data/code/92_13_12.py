class BooleanNegator:
    TRUE = 1
    FALSE = 0
    
    @staticmethod
    def find_opposite_truth_value(value: bool) -> bool:
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.find_opposite_truth_value(True))
    print(negator.find_opposite_truth_value(False))