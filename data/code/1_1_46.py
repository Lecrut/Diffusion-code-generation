class WeightConverter:
    CONVERSION_FACTORS = {
        'kg': 1,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495,
        'ton': 1000
    }

    @staticmethod
    def convert_to_kilograms(weights):
        converted_weights = []
        for weight in weights:
            try:
                value, unit = weight.split()
                value = float(value)
                if unit not in WeightConverter.CONVERSION_FACTORS:
                    raise ValueError(f"Unsupported unit: {unit}")
                converted_weight = value * WeightConverter.CONVERSION_FACTORS[unit]
                converted_weights.append(converted_weight)
            except (ValueError, TypeError) as e:
                print(f"Error processing weight '{weight}': {e}")
        return converted_weights

if __name__ == '__main__':
    sample_weights = [
        "10 kg",
        "500 g",
        "2 lb",
        "8 oz",
        "0.5 ton"
    ]
    converter = WeightConverter()
    print(converter.convert_to_kilograms(sample_weights))