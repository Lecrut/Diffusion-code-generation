class UnitConverter:
    FEET_TO_MICROMETERS_FACTOR = 304800

    @staticmethod
    def feet_to_micrometers(feet):
        return feet * UnitConverter.FEET_TO_MICROMETERS_FACTOR

if __name__ == '__main__':
    print(UnitConverter.feet_to_micrometers(1))
    print(UnitConverter.feet_to_micrometers(5))
    print(UnitConverter.feet_to_micrometers(10))