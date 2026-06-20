class TruthInverter:
    @staticmethod
    def find_opposite_truth(truth):
        return not truth

if __name__ == '__main__':
    inverter = TruthInverter()
    sample1 = True
    result1 = inverter.find_opposite_truth(sample1)
    print(f"Opposite of {sample1} is {result1}")
    sample2 = False
    result2 = inverter.find_opposite_truth(sample2)
    print(f"Opposite of {sample2} is {result2}")