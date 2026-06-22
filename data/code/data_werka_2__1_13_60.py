class WeightConverter:
    KG_TO_LB = 2.20462

    @staticmethod
    def convert_kg_to_lb(weights_kg):
        return [WeightConverter.KG_TO_LB * weight for weight in weights_kg]

if __name__ == '__main__':
    sample_weights = [1, 5, 10, 20]
    converted_weights = WeightConverter.convert_kg_to_lb(sample_weights)
    print(converted_weights)