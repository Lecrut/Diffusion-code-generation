class WeightConverter:
    KILOGRAMS_TO_OUNCES = 35.274

    @staticmethod
    def convert_weights(weight_dict):
        result = {}
        for item, weight in weight_dict.items():
            if isinstance(weight, dict):
                result[item] = WeightConverter.convert_weights(weight)
            else:
                result[item] = weight * WeightConverter.KILOGRAMS_TO_OUNCES
        return result

if __name__ == '__main__':
    sample_data = {
        'apple': 0.5,
        'banana': {
            'small': 0.2,
            'large': 0.3
        },
        'orange': 0.7
    }
    converted_data = WeightConverter.convert_weights(sample_data)
    print(converted_data)