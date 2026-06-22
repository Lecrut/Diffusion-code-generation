class DistanceConverter:
    M_TO_KM = 1 / 1000
    KM_TO_M = 1000

    @staticmethod
    def convert(value, unit):
        if unit == 'm_to_km':
            return value * DistanceConverter.M_TO_KM
        elif unit == 'km_to_m':
            return value * DistanceConverter.KM_TO_M
        else:
            raise ValueError("Unsupported unit. Use 'm_to_km' for meters to kilometers or 'km_to_m' for kilometers to meters.")

if __name__ == '__main__':
    sample_values = [
        (1500, 'm_to_km'),
        (2.5, 'km_to_m')
    ]
    for value, unit in sample_values:
        converted_value = DistanceConverter.convert(value, unit)
        print(f"{value} {unit.replace('_', ' to ')} is {converted_value} {'kilometers' if unit == 'm_to_km' else 'meters'}")