class Square:
    _UNITS = {
        'cm': 'square centimeters',
        'm': 'square meters',
        'in': 'square inches'
    }

    def __init__(self, side_length, unit='cm'):
        if unit not in self._UNITS:
            raise KeyError(f"Unsupported unit: {unit}")
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        self._side = side_length
        self._unit = unit

    def get_area(self):
        return self._side * self._side

    def get_unit_description(self):
        return self._UNITS[self._unit]

if __name__ == '__main__':
    shape = Square(7, 'm')
    area_value = shape.get_area()
    print(f"{area_value} {shape.get_unit_description()}")