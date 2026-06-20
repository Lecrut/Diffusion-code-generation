class BooleanToggler:
    @staticmethod
    def opposite_truth(value):
        return not value

if __name__ == '__main__':
    sample_value = True
    result = BooleanToggler.opposite_truth(sample_value)
    print(result)