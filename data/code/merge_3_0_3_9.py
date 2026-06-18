class UnitConverter:
    # Conversion factors to meters (1 unit = factor * meter)
    METERS_PER_METER = 1.0
    FEET_PER_METER = 3.28084
    KILOMETERS_PER_METER = 0.001
    
    Meters_to_Feet = lambda self, meters: meters * self.FEET_PER_METER
    Meters_to_Kilometers = lambda self, meters: meters * self.KILOMETERS_PER_METER

def convert_meters_to_feet(meters):
    return meters * 3.28084

if __name__ == '__main__':
    # Sample values for testing conversions without interactive input
    sample_meters = [10, 50, 100]
    
    print("Converting Meters to Feet:")
    for m in sample_meters:
        feet = convert_meters_to_feet(m)
        print(f"{m} meters is approximately {feet:.2f} feet")

    # Note: The class constants are defined but the specific instance methods were not fully utilized 
    # to keep the code simple and runnable as requested, focusing on direct conversion logic.