class BooleanOperations:
    @staticmethod
    def find_opposite_truth(value):
        return not value

if __name__ == '__main__':
    sample_values = [True, False]
    for value in sample_values:
        print(BooleanOperations.find_opposite_truth(value))