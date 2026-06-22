class UnitConverter:
    YARDS_TO_KILOMETERS = 0.0009144

    @staticmethod
    def convert_yards_to_kilometers(yards):
        return yards * UnitConverter.YARDS_TO_KILOMETERS
if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.convert_yards_to_kilometers(100)
    print(result)