class VolumeConverter:
    """A class to convert between volume units including liters/milliliters 
    and cubic meters/cubic inches."""
    
    def __init__(self):
        # Conversion factors are defined here for clarity and reuse
        self.LITERS_TO_MILLILITERS = 1000.0
        
        # Cubic meter to cubic inch conversion factor:
        # 1 m^3 = (39.3701 inches)^3 ≈ 61023.744 in^3
        self.CUBIC_METERS_TO_CUBIC_INCHES = 61023.744
        
    def liters_to_milliliters(self, value: float) -> float:
        """Converts a volume from liters to milliliters."""
        return value * self.LITERS_TO_MILLILITERS
    
    def milliliters_to_liters(self, value: float) -> float:
        """Converts a volume from milliliters to liters."""
        return value / self.LITERS_TO_MILLILITERS
    
    def cubic_meters_to_cubic_inches(self, value: float) -> float:
        """Converts a volume from cubic meters to cubic inches."""
        return value * self.CUBIC_METERS_TO_CUBIC_INCHES
    
    def cubic_inches_to_cubic_meters(self, value: float) -> float:
        """Converts a volume from cubic inches to cubic meters."""
        return value / self.CUBIC_METERS_TO_CUBIC_INCHES

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    converter = VolumeConverter()
    
    print("Volume Conversion Results")
    print("-" * 30)
    
    # Sample conversions: Liters to Milliliters and vice versa
    liters_input = 2.5
    ml_output = converter.liters_to_milliliters(liters_input)
    print(f"{liters_input} L -> {ml_output:.4f} mL")
    
    ml_input = 7500
    l_output = converter.milliliters_to_liters(ml_input)
    print(f"{ml_input} mL -> {l_output:.2f} L")
    
    # Sample conversions: Cubic Meters to Cubic Inches and vice versa
    m3_input = 1.5
    in3_output = converter.cubic_meters_to_cubic_inches(m3_input)
    print(f"{m3_input} m³ -> {in3_output:.2f} in³")
    
    in3_input = 100000
    m3_output = converter.cubic_inches_to_cubic_meters(in3_input)
    print(f"{in3_input} in³ -> {m3_output:.4f} m³")