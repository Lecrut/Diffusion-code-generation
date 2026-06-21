class WeightComparator:

    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def validate_weights(self):
        if self.weight1 < 0 or self.weight2 < 0:
            raise ValueError('Weights cannot be negative')
        return True

    def compute_difference(self):
        self.validate_weights()
        return abs(self.weight1 - self.weight2)

    def display_result(self):
        difference = self.compute_difference()
        print(f'The weight difference is: {difference}')
if __name__ == '__main__':
    comparator = WeightComparator(15.5, 10.2)
    try:
        comparator.display_result()
    except ValueError as e:
        print(e)
    comparator2 = WeightComparator(0, 5)
    try:
        comparator2.display_result()
    except ValueError as e:
        print(e)
    comparator3 = WeightComparator(-1, 10)
    try:
        comparator3.display_result()
    except ValueError as e:
        print(e)