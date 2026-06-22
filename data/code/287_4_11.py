class WeightConverter:
    def convert_to_ounces(self, weights):
        ounces = []
        for weight, unit in weights:
            if unit == 'kg':
                ounces.append(weight * 35.274)
            elif unit == 'lb':
                ounces.append(weight * 16)
            else:
                raise ValueError(f"Unsupported unit: {unit}")
        return ounces

if __name__ == '__main__':
    converter = WeightConverter()
    weights_pounds = [('10', 'lb'), ('2.5', 'lb')]
    weights_kg = [('1', 'kg'), ('0.5', 'kg')]
    combined_weights_ounces = [converter.convert_to_ounces(weights_pounds), converter.convert_to_ounces(weights_kg)]
    print(combined_weights_ounces)