class PressureConverter:
    PASCALS_TO_PSI = 0.000145038
    PASCALS_TO_ATM = 9.86923e-06

    @staticmethod
    def convert(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'pascal':
            if to_unit == 'psi':
                return value * PressureConverter.PASCALS_TO_PSI
            elif to_unit == 'atm':
                return value * PressureConverter.PASCALS_TO_ATM
        elif from_unit == 'psi':
            if to_unit == 'pascal':
                return value / PressureConverter.PASCALS_TO_PSI
            elif to_unit == 'atm':
                return value / 14.695978
        elif from_unit == 'atm':
            if to_unit == 'pascal':
                return value / PressureConverter.PASCALS_TO_ATM
            elif to_unit == 'psi':
                return value * 14.695978
if __name__ == '__main__':
    converter = PressureConverter()
    print(converter.convert(100, 'pascal', 'psi'))
    print(converter.convert(1, 'psi', 'atm'))