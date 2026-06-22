class VolumeCalculator:
    _CONVERSION_TO_LITERS = {
        "mL": 0.001,
        "L": 1.0,
        "gal": 3.78541,
        "qt": 0.946353,
        "pt": 0.473176,
        "cup": 0.236588,
        "fl_oz": 0.0295735,
        "in3": 0.0163871,
        "cm3": 0.001,
    }

    def __init__(self):
        self._measurements = []

    def add_measurements(self, volumes):
        self._measurements = list(volumes)

    def get_total_volume(self, target_unit):
        if target_unit not in self._CONVERSION_TO_LITERS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        total_liters = sum(
            (vol * self._CONVERSION_TO_LITERS[unit] for vol, unit in self._measurements)
        )
        
        conversion_factor = self._CONVERSION_TO_LITERS[target_unit]
        return total_liters / conversion_factor

if __name__ == '__main__':
    calculator = VolumeCalculator()
    data = [
        (1000, "mL"),
        (2, "L"),
        (1, "gal"),
        (500, "mL")
    ]
    calculator.add_measurements(data)
    
    total_liters = calculator.get_total_volume("L")
    total_gallons = calculator.get_total_volume("gal")
    
    print(total_liters)
    print(total_gallons)