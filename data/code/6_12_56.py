class WeightDifferencer:
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def calculate_difference(self):
        return abs(self.weight1 - self.weight2)

if __name__ == '__main__':
    ALICE_WEIGHT = 75.5
    BOB_WEIGHT = 68.3
    differencer = WeightDifferencer(ALICE_WEIGHT, BOB_WEIGHT)
    difference = differencer.calculate_difference()
    print(difference)