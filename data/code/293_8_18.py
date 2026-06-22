class PressureConverter:
    PASCAL_TO_PSI = 1 / 6894.75729313
    PSI_TO_PASCAL = 6894.75729313
    PASCAL_TO_ATMOSPHERE = 1 / 101325
    ATMOSPHERE_TO_PASCAL = 101325

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        elif from_unit == 'pascal':
            if to_unit == 'psi':
                return value * PressureConverter.PASCAL_TO_PSI
            elif to_unit == 'atmosphere':
                return value * PressureConverter.PASCAL_TO_ATMOSPHERE
        elif from_unit == 'psi':
            if to_unit == 'pascal':
                return value * PressureConverter.PSI_TO_PASCAL
            elif to_unit == 'atmosphere':
                return value * (PressureConverter.PSI_TO_PASCAL * PressureConverter.PASCAL_TO_ATMOSPHERE)
        elif from_unit == 'atmosphere':
            if to_unit == 'pascal':
                return value * PressureConverter.ATMOSPHERE_TO_PASCAL
            elif to_unit == 'psi':
                return value * PressureConverter.ATMOSPHERE_TO_PASCAL / PressureConverter.PSI_TO_PASCAL
if __name__ == '__main__':
    converter = PressureConverter()
    print(converter.convert(1, 'pascal', 'psi'))
    print(converter.convert(1, 'psi', 'atmosphere'))