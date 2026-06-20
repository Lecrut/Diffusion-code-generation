class UnitConverter:
    CONVERSION_FACTOR = 3.28084

    @staticmethod
    def meters_to_feet(value: float) -> float:
        return value * UnitConverter.CONVERSION_FACTOR

if __name__ == '__main__':
    input_value = 10
    output_value = UnitConverter.meters_to_feet(input_value)
    print(output_value)