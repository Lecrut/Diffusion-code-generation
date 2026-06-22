class WeightConverter:

    def __init__(self, ratios):
        self.ratios = ratios

    def convert_to_weights(self, total_weight):
        ratio_sum = sum(self.ratios)
        if ratio_sum == 0:
            raise ValueError('Sum of ratios must not be zero.')
        return [ratio / ratio_sum * total_weight for ratio in self.ratios]
if __name__ == '__main__':
    sample_ratios = [1, 2, 3]
    total_weight = 60
    converter = WeightConverter(sample_ratios)
    absolute_weights = converter.convert_to_weights(total_weight)
    print(absolute_weights)
    another_ratios = [4, 5, 1]
    another_total_weight = 100
    another_converter = WeightConverter(another_ratios)
    another_absolute_weights = another_converter.convert_to_weights(another_total_weight)
    print(another_absolute_weights)