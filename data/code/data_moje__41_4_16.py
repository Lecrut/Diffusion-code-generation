DIAGONAL_UNITS = {
    "cm": "square cm",
    "m": "square m",
    "in": "square inches",
    "ft": "square feet"
}

def compute_rhombus_area(diagonal_a, diagonal_b, unit_label):
    if unit_label not in DIAGONAL_UNITS:
        raise ValueError("Unsupported unit")
    area = 0.5 * diagonal_a * diagonal_b
    return area

class RhombusCalculator:
    def __init__(self, d_one, d_two, unit):
        self.diagonal_one = d_one
        self.diagonal_two = d_two
        self.unit = unit

    def get_area(self):
        return compute_rhombus_area(self.diagonal_one, self.diagonal_two, self.unit)

    def get_unit_label(self):
        return DIAGONAL_UNITS.get(self.unit, "units")

if __name__ == '__main__':
    d1_val = 12.5
    d2_val = 18.0
    u_label = "cm"
    calc = RhombusCalculator(d1_val, d2_val, u_label)
    result = calc.get_area()
    unit_out = calc.get_unit_label()
    print(f"{result} {unit_out}")