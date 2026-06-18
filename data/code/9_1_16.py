import math

class VolumeConverter:
    """
    A class to convert between volume units: liters, milliliters, cubic meters, 
    and cubic inches. It is designed to be reusable with static conversion factors.
    
    Attributes:
        None (uses internal constants for conversions)
        
    Methods:
        l_to_ml(liters): Converts liters to milliliters.
        ml_to_l(milliliters): Converts milliliters to liters.
        m3_to_inch_cubic(cubic_meters): Converts cubic meters to cubic inches.
        inch_cubic_to_m3(inch_vol): Converts cubic inches to cubic meters.
    """

    # Conversion factors (1 unit = X units of target)
    FACTORS = {
        'L_TO_ML': 1000,          # 1 Liter = 1000 Milliliters
        'ML_TO_L': 0.001,         # 1 Milliliter = 0.001 Liters
        'M3_TO_INCH_CUBIC': 6102374.409473178, # ~1 m³ ≈ 6102374.4 in³
    }

    def __init__(self):
        """Initialize the VolumeConverter instance."""
        pass
    
    def l_to_ml(self, liters: float) -> float:
        """Converts a volume from liters to milliliters.
        
        Args:
            liters (float): The volume in liters.
            
        Returns:
            float: The equivalent volume in milliliters.
        """
        return self.FACTORS['L_TO_ML'] * liters

    def ml_to_l(self, milliliters: float) -> float:
        """Converts a volume from milliliters to liters.
        
        Args:
            milliliters (float): The volume in milliliters.
            
        Returns:
            float: The equivalent volume in liters.
        """
        return self.FACTORS['ML_TO_L'] * milliliters

    def m3_to_inch_cubic(self, cubic_meters: float) -> float:
        """Converts a volume from cubic meters to cubic inches.
        
        Args:
            cubic_meters (float): The volume in cubic meters.
            
        Returns:
            float: The equivalent volume in cubic inches.
        """
        return self.FACTORS['M3_TO_INCH_CUBIC'] * cubic_meters

    def inch_cubic_to_m3(self, inch_vol: float) -> float:
        """Converts a volume from cubic inches to cubic meters.
        
        Args:
            inch_vol (float): The volume in cubic inches.
            
        Returns:
            float: The equivalent volume in cubic meters.
        """
        # Using the inverse of m3_to_inch_cubic factor derived directly for precision or dividing by original constant
        return inch_vol / self.FACTORS['M3_TO_INCH_CUBIC']

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    
    converter = VolumeConverter()
    
    # Sample 1: Liters to Milliliters
    liters_input = 2.5
    ml_result = converter.l_to_ml(liters_input)
    print(f"{liters_input} Liter(s) is equal to {ml_result:.4f} Milliliter(s).")

    # Sample 2: Milliliters to Liters
    ml_input = 100.5
    l_result = converter.ml_to_l(ml_input)
    print(f"{ml_input} Milliliter(s) is equal to {l_result:.4f} Liter(s).")

    # Sample 3: Cubic Meters to Cubic Inches
    m3_input = 10.0
    inch_cubic_result = converter.m3_to_inch_cubic(m3_input)
    print(f"{m3_input} Cubic Meter(s) is equal to {inch_cubic_result:.4f} Cubic Inch(es).")

    # Sample 4: Cubic Inches to Cubic Meters (Inverse check)
    inch_cubic_check = converter.m3_to_inch_cubic(m3_input * 0.1) # Calculate a known cubic inch value from m3 and pass it back
    actual_m3_from_inches = converter.inch_cubic_to_m3(inch_cubic_check)
    
    print(f"{m3_input} Cubic Meter(s) converted to {inch_cubic_result:.4f} Cubic Inch(es).")
    print(f"Converting that specific value back: {actual_m3_from_inches:.10f} Cubic Meters.")