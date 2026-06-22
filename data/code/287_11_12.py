class WeightConverter:
    CONVERSION_FACTORS = {'kg': 1, 'lbs': 0.453592}

    @staticmethod
    def convert_weight(weight, unit):
        if unit not in WeightConverter.CONVERSION_FACTORS:
            raise ValueError(f"Unknown unit: {unit}")
        return weight * WeightConverter.CONVERSION_FACTORS[unit]

    @classmethod
    def convert_weights(cls, raw_weights):
        results = []
        for weight, unit in raw_weights:
            converted_weight = cls.convert_weight(weight, unit)
            results.append((weight, unit, converted_weight))
        return results

    @staticmethod
    def print_table(weights):
        headers = ["Original Value", "Unit", "Converted (kg)"]
        print("\t".join(headers))
        for weight in weights:
            print("\t".join(map(str, weight)))

if __name__ == '__main__':
    raw_data = [('70', 'kg'), ('154', 'lbs'), ('60', 'kg')]
    converter = WeightConverter()
    converted_weights = converter.convert_weights(raw_data)
    converter.print_table(converted_weights)