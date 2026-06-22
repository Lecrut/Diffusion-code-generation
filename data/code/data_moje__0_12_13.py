class UnitConverter:
    _CM_TO_INCHES = 1 / 2.54

    @staticmethod
    def centimeters_to_inches(cm: float) -> float:
        return cm * UnitConverter._CM_TO_INCHES

if __name__ == '__main__':
    converter = UnitConverter()
    result = converter.centimeters_to_inches(50)
    print(result)