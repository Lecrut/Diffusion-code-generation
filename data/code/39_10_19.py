UNIT_CONVERSION = {"cubic": 1, "milli_cubic": 1000, "micro_cubic": 1000000}

class Prism:
    def __init__(self, base_area, height, unit_type="cubic"):
        self.base_area = base_area
        self.height = height
        self.unit_type = unit_type

    def calculate_volume(self):
        raw_volume = self.base_area * self.height
        conversion_factor = UNIT_CONVERSION.get(self.unit_type, 1)
        return raw_volume * conversion_factor

    def get_dimensions_summary(self):
        return {
            "area": self.base_area,
            "height": self.height,
            "unit": self.unit_type
        }

if __name__ == '__main__':
    sample_base = 15.5
    sample_height = 20
    sample_unit = "milli_cubic"
    
    prism_instance = Prism(sample_base, sample_height, sample_unit)
    computed_volume = prism_instance.calculate_volume()
    print(computed_volume)