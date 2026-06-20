class BooleanToggle:
    @staticmethod
    def opposite_truth(value):
        return not value

if __name__ == '__main__':
    sample_value = True
    print(BooleanToggle.opposite_truth(sample_value))
    another_sample = False
    print(BooleanToggle.opposite_truth(another_sample))