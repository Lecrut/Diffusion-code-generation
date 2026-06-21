from typing import Union
L_TO_ML = 1000
ML_TO_L = 1 / L_TO_ML
M3_TO_L = 1000
L_TO_M3 = 1 / M3_TO_L
L_TO_GAL = 0.264172
GAL_TO_L = 1 / L_TO_GAL

class VolumeConverter:

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit.lower()

    def to_liters(self) -> float:
        if self.unit == 'l':
            return self.value
        elif self.unit == 'ml':
            return self.value / L_TO_ML
        elif self.unit == 'm3':
            return self.value * M3_TO_L
        elif self.unit == 'gal':
            return self.value * GAL_TO_L
        else:
            raise ValueError(f'Unsupported unit: {self.unit}')

    def to_milliliters(self) -> float:
        return self.to_liters() * L_TO_ML

    def to_cubic_meters(self) -> float:
        return self.to_liters() / M3_TO_L

    def to_gallons(self) -> float:
        return self.to_liters() / GAL_TO_L

def convert_volume(value: Union[float, int], from_unit: str, to_unit: str) -> float:
    converter = VolumeConverter(value, from_unit)
    if to_unit.lower() == 'l':
        return converter.to_liters()
    elif to_unit.lower() == 'ml':
        return converter.to_milliliters()
    elif to_unit.lower() == 'm3':
        return converter.to_cubic_meters()
    elif to_unit.lower() == 'gal':
        return converter.to_gallons()
    else:
        raise ValueError(f'Unsupported unit: {to_unit}')
if __name__ == '__main__':
    sample_values = [(1, 'L'), (500, 'ml'), (2, 'm3'), (3.78541, 'gal')]
    for value, unit in sample_values:
        converter = VolumeConverter(value, unit)
        print(f'{value} {unit} is {converter.to_liters()} L')
        print(f'{value} {unit} is {converter.to_milliliters()} mL')
        print(f'{value} {unit} is {converter.to_cubic_meters()} m³')
        print(f'{value} {unit} is {converter.to_gallons()} gal')
    print(convert_volume(1, 'L', 'gal'))
    print(convert_volume(500, 'ml', 'm3'))