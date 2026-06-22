class VolumeCalculator:
    UNIT_FACTORS = {
        "ml": 1.0,
        "l": 1000.0,
        "us_fl_oz": 29.5735,
        "gal": 3785.41,
        "cup": 236.588,
        "pt": 473.176,
        "qt": 946.353,
        "m3": 1000000.0,
        "cm3": 1.0
    }

    def calculate_total(self, measurements: list, target_unit: str) -> float:
        if target_unit not in self.UNIT_FACTORS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        base_ml_values = [
            value * self.UNIT_FACTORS[unit] 
            for value, unit in measurements
            if unit in self.UNIT_FACTORS
        ]
        
        total_base_ml = sum(base_ml_values)
        return total_base_ml / self.UNIT_FACTORS[target_unit]

if __name__ == "__main__":
    samples = [
        (100, "ml"),
        (1, "l"),
        (32, "us_fl_oz"),
        (2, "cup"),
        (0.5, "gal")
    ]
    calculator = VolumeCalculator()
    result = calculator.calculate_total(samples, "ml")
    print(f"Total volume in ml: {result}")
    
    result_gal = calculator.calculate_total(samples, "gal")
    print(f"Total volume in gal: {result_gal}")
    
    result_l = calculator.calculate_total(samples, "l")
    print(f"Total volume in l: {result_l}")