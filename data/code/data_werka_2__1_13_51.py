class WeightConverter:
    KG_TO_LB_CONVERSION_FACTOR = 2.20462

    @staticmethod
    def convert_kg_to_lb(weights_kg):
        return [weight * WeightConverter.KG_TO_LB_CONVERSION_FACTOR for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [2, 7, 15, 30]
    converter = WeightConverter()
    converted_weights = converter.convert_kg_to_lb(sample_weights)
    print(converted_weights)