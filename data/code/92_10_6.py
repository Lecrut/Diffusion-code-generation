class BooleanNegator:
    @staticmethod
    def find_opposite_truth(value):
        return not value

if __name__ == '__main__':
    negator = BooleanNegator()
    print(negator.find_opposite_truth(True))
    print(negator.find_opposite_truth(False))