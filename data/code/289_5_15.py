class DistanceConverter:
    CONVERSIONS = {
        'yd': 0.9144,
        'm': 1.0
    }

    @staticmethod
    def convert(value, from_unit):
        if value < 0:
            raise ValueError("Value must be non-negative")
        if from_unit not in DistanceConverter.CONVERSIONS:
            raise ValueError("Invalid unit specified")
        return value * DistanceConverter.CONVERSIONS[from_unit]

if __name__ == '__main__':
    print(f"10 yd to m: {DistanceConverter.convert(10, 'yd'):.2f}")