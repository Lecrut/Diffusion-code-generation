class WeightConverter:
    KG_TO_LB = 2.20462

    @staticmethod
    def convert(weights_kg):
        return [WeightConverter.convert_single(weight) for weight in weights_kg]

    @staticmethod
    def convert_single(weight_kg):
        return weight_kg * WeightConverter.KG_TO_LB

if __name__ == '__main__':
    sample_weights = [2.5, 7.5, 15, 30]
    converter = WeightConverter()
    converted_weights = converter.convert(sample_weights)
    print(converted_weights)