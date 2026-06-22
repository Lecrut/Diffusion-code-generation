class UnitConverter:
    GALLON_TO_LITER = 3.78541
    LITER_TO_GALLON = 1 / GALLON_TO_LITER

    @staticmethod
    def convert(value: float, from_unit: str, to_unit: str) -> float:
        if from_unit == 'gallon':
            if to_unit == 'liter':
                return value * UnitConverter.GALLON_TO_LITER
            else:
                raise ValueError("Invalid conversion to unit")
        elif from_unit == 'liter':
            if to_unit == 'gallon':
                return value * UnitConverter.LITER_TO_GALLON
            else:
                raise ValueError("Invalid conversion to unit")
        else:
            raise ValueError("Invalid conversion from unit")

if __name__ == '__main__':
    print(f"10 gallon to liter: {UnitConverter.convert(10.0, 'gallon', 'liter'):.2f}")
    print(f"5 liter to gallon: {UnitConverter.convert(5.0, 'liter', 'gallon'):.2f}")