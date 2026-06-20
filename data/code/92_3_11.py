class BoolInverter:
    @staticmethod
    def invert_truth_values(boolean_list):
        return [not x for x in boolean_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    inverted_values = BoolInverter.invert_truth_values(sample_values)
    print(inverted_values)