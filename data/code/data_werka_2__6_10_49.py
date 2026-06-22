class WeightDifferencer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def compute_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    SAMPLE_WEIGHT_1 = 95.0
    SAMPLE_WEIGHT_2 = 88.5
    differencer = WeightDifferencer(SAMPLE_WEIGHT_1, SAMPLE_WEIGHT_2)
    difference = differencer.compute_difference()
    print(difference)