class DistanceConverter:
    def __init__(self):
        self.km_to_meters = 1000.0
        self.miles_to_meters = 1609.344
        self.feet_to_meters = 0.3048
        self.inches_to_meters = 0.0254
        self.centimeters_to_meters = 0.01
        self.yards_to_meters = 0.9144
        self.kilometers_to_meters = 1000.0
        self.meters_to_meters = 1.0
        
        self.units_to_factor = {
            "km": self.kilometers_to_meters,
            "kilometer": self.kilometers_to_meters,
            "kilometers": self.kilometers_to_meters,
            "m": self.meters_to_meters,
            "meter": self.meters_to_meters,
            "meters": self.meters_to_meters,
            "mi": self.miles_to_meters,
            "mile": self.miles_to_meters,
            "miles": self.miles_to_meters,
            "ft": self.feet_to_meters,
            "foot": self.feet_to_meters,
            "feet": self.feet_to_meters,
            "in": self.inches_to_meters,
            "inch": self.inches_to_meters,
            "inches": self.inches_to_meters,
            "cm": self.centimeters_to_meters,
            "centimeter": self.centimeters_to_meters,
            "centimeters": self.centimeters_to_meters,
            "yd": self.yards_to_meters,
            "yard": self.yards_to_meters,
            "yards": self.yards_to_meters
        }

    def convert(self, value, from_unit, to_unit):
        from_lower = from_unit.lower().strip()
        to_lower = to_unit.lower().strip()
        
        if from_lower not in self.units_to_factor:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_lower not in self.units_to_factor:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        if value < 0:
            raise ValueError("Distance cannot be negative")
            
        meters = value * self.units_to_factor[from_lower]
        result = meters / self.units_to_factor[to_lower]
        return result

def main():
    converter = DistanceConverter()
    
    result_km_to_miles = converter.convert(10, "km", "mi")
    print(f"10 km = {result_km_to_miles} mi")
    
    result_miles_to_km = converter.convert(6.21371, "mi", "km")
    print(f"6.21371 mi = {result_miles_to_km} km")
    
    result_ft_to_cm = converter.convert(1, "ft", "cm")
    print(f"1 ft = {result_ft_to_cm} cm")

if __name__ == '__main__':
    main()