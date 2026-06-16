class UnitConverter:
    @staticmethod
    def convert_mass(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'kg' and to_unit == 'lb':
            return value * 2.2046226218
        elif from_unit == 'lb' and to_unit == 'kg':
            return value / 2.2046226218
        return None
    @staticmethod
    def convert_length(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == 'm' and to_unit == 'ft':
            return value * 3.28084
        elif from_unit == 'ft' and to_unit == 'm':
            return value / 3.28084
        return None
if __name__ == '__main__':
    mass_value = 10
    mass_from = 'kg'
    mass_to = 'lb'
    mass_result = UnitConverter.convert_mass(mass_value, mass_from, mass_to)
    print(f"{mass_value} {mass_from} is equal to {mass_result:.2f} {mass_to}")
    length_value = 10
    length_from = 'm'
    length_to = 'ft'
    length_result = UnitConverter.convert_length(length_value, length_from, length_to)
    print(f"{length_value} {length_from} is equal to {length_result:.2f} {length_to}")
    mass_round_trip = 50
    mass_result_round_trip = UnitConverter.convert_mass(mass_round_trip, 'lb', 'kg')
    print(f"{mass_round_trip} lb is equal to {mass_result_round_trip:.2f} kg")
    length_round_trip = 100
    length_result_round_trip = UnitConverter.convert_length(length_round_trip, 'ft', 'm')
    print(f"{length_round_trip} ft is equal to {length_result_round_trip:.2f} m")