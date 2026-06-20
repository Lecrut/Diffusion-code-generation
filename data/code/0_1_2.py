class UnitConverter:
    METER_TO_FEET = 3.28084
    METER_TO_KILOMETER = 0.001

    @classmethod
    def meters_to_feet(cls, meters):
        return meters * cls.METER_TO_FEET

    @classmethod
    def meters_to_kilometers(cls, meters):
        return meters * cls.METER_TO_KILOMETER

    @classmethod
    def feet_to_meters(cls, feet):
        return feet / cls.METER_TO_FEET

    @classmethod
    def kilometers_to_meters(cls, kilometers):
        return kilometers / cls.METER_TO_KILOMETER

    @classmethod
    def feet_to_kilometers(cls, feet):
        return cls.feet_to_meters(feet) * cls.METER_TO_KILOMETER

    @classmethod
    def kilometers_to_feet(cls, kilometers):
        return cls.kilometers_to_meters(kilometers) * cls.METER_TO_FEET

if __name__ == '__main__':
    converter = UnitConverter()
    result_m_to_f = converter.meters_to_feet(10)
    result_m_to_k = converter.meters_to_kilometers(10)
    result_f_to_m = converter.feet_to_meters(32.8084)
    result_k_to_m = converter.kilometers_to_meters(5)
    result_f_to_k = converter.feet_to_kilometers(1000)
    result_k_to_f = converter.kilometers_to_feet(1)

    print(result_m_to_f)
    print(result_m_to_k)
    print(result_f_to_m)
    print(result_k_to_m)
    print(result_f_to_k)
    print(result_k_to_f)