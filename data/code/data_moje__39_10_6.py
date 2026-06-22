class GeometricPrism:
    _positive_check_threshold = 1e-9

    def __init__(self, base_area, altitude):
        self._validate_positive(base_area, "base_area")
        self._validate_positive(altitude, "altitude")
        self._base_area = base_area
        self._altitude = altitude

    def _validate_positive(self, value, label):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{label} must be a number")
        if value <= self._positive_check_threshold:
            raise ValueError(f"{label} must be strictly positive")

    def compute_volume(self):
        return self._base_area * self._altitude

def calculate_prism_volume(base_area_val, height_val):
    p = GeometricPrism(base_area_val, height_val)
    return p.compute_volume()

if __name__ == '__main__':
    result = calculate_prism_volume(12.5, 8.0)
    print(result)