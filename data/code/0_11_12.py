class LengthConverter:
    METERS_TO_FEET = 3.28084

    def convert_meters_to_feet(self, meters: float) -> float:
        return meters * self.METERS_TO_FEET

if __name__ == '__main__':
    converter = LengthConverter()
    result = converter.convert_meters_to_feet(10)
    print(result)