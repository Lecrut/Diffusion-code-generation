import csv

class WeightConverter:
    CONVERSION_FACTORS = {'kg_to_lb': 2.20462, 'lb_to_kg': 0.453592, 'oz_to_lb': 16}

    @staticmethod
    def convert(value, from_unit):
        if from_unit == 'kg':
            return value * WeightConverter.CONVERSION_FACTORS['kg_to_lb']
        elif from_unit == 'lb':
            return value
        elif from_unit == 'oz':
            return value / WeightConverter.CONVERSION_FACTORS['oz_to_lb']
        else:
            raise ValueError(f'Unsupported unit: {from_unit}')

    @staticmethod
    def convert_weights(input_file, output_file):
        with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                weight_value = float(row['weight'])
                weight_unit = row['unit']
                new_weight = WeightConverter.convert(weight_value, weight_unit)
                row['weight'] = new_weight
                row['unit'] = 'lb'
                writer.writerow(row)
if __name__ == '__main__':
    converter = WeightConverter()
    print(converter.convert(1, 'kg'))
    print(converter.convert(16, 'oz'))
    converter.convert_weights('sample_input.csv', 'output.csv')