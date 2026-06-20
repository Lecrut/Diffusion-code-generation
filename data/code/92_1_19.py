class TruthNegator:
    def find_opposite_truth(self, truth):
        return not truth

if __name__ == '__main__':
    negator = TruthNegator()
    sample1 = True
    result1 = negator.find_opposite_truth(sample1)
    print(f"Opposite of {sample1} is {result1}")
    sample2 = False
    result2 = negator.find_opposite_truth(sample2)
    print(f"Opposite of {sample2} is {result2}")