class OppositeTruth:
    @staticmethod
    def find_opposite_truth(truth):
        return not truth

if __name__ == '__main__':
    sample_values = [True, False]
    opposite_truth_instance = OppositeTruth()
    for value in sample_values:
        result = opposite_truth_instance.find_opposite_truth(value)
        print(f"Opposite of {value} is {result}")