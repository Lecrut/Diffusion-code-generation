import json

class WeightConverter:
    def __init__(self):
        self.conversion_factors = {
            'kg': 2.20462,
            'lbs': 1.0,
            'oz': 0.0625
        }

    def convert_weights(self, data):
        for item in data:
            if 'weight' in item and isinstance(item['weight'], dict):
                unit = item['weight']['unit']
                value = item['weight']['value']
                converted_value = value * self.conversion_factors[unit]
                item['weight'] = {'unit': 'lbs', 'value': converted_value}
        return data

if __name__ == '__main__':
    converter = WeightConverter()
    sample_data = [
        {
            "item": "apple",
            "weight": {"value": 1, "unit": "kg"}
        },
        {
            "item": "banana",
            "weight": {"value": 0.5, "unit": "oz"}
        }
    ]
    converted_data = converter.convert_weights(sample_data)
    print(json.dumps(converted_data, indent=4))