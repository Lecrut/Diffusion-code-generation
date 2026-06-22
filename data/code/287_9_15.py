class WeightConverter:
    OUNCES_PER_KILOGRAM = 35.274

    @staticmethod
    def convert_weights(input_dict):
        output_dict = {}
        for item, weight in input_dict.items():
            if isinstance(weight, dict):
                output_dict[item] = WeightConverter.convert_weights(weight)
            else:
                output_dict[item] = weight * WeightConverter.OUNCES_PER_KILOGRAM
        return output_dict

if __name__ == '__main__':
    sample_data = {
        'apples': 2,
        'oranges': 1.5,
        'nested': {
            'bananas': 3,
            'grapes': 0.2
        }
    }
    converted_data = WeightConverter.convert_weights(sample_data)
    print(converted_data)