PRISM_UNITS = {
    "metric": 1.0,
    "imperial": 1.0,
    "cgs": 1.0
}

class Prism:
    def __init__(self, base_area, height, unit_type="metric"):
        self.base_area = base_area
        self.height = height
        self.unit_type = unit_type
        self.scale_factor = PRISM_UNITS.get(unit_type, 1.0)

    def volume(self):
        raw_vol = self.base_area * self.height
        return raw_vol * self.scale_factor

    def describe(self):
        return f"Prism with base {self.base_area}, height {self.height}, volume {self.volume()}"

if __name__ == '__main__':
    p = Prism(12.5, 8.0, "metric")
    print(p.volume())
    print(p.describe())