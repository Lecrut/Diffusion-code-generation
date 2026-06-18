class WeightConverter:
    def __init__(self, value):
        self.value = value  # Store original value in base unit (assumed to be pounds internally if not specified)
    
    def convert_to_kg(self):
        """Convert weight from pounds to kilograms."""
        return round(self.value * 0.45359237, 6)

if __name__ == '__main__':
    # Sample hard-coded values without user input or CLI arguments
    
    # Example 1: Convert a specific stored value (stored as lbs) to kg
    sample_weight_lbs = 10.0 
    converter_sample_1 = WeightConverter(sample_weight_lbs)
    
    result_kg_1 = converter_sample_1.convert_to_kg()
    print(f"Stored weight ({sample_weight_lbs} lbs) converted to: {result_kg_1} kg")

    # Example 2: Another dynamic conversion for a different value
    sample_weight_lbs_2 = 50.5 
    converter_sample_2 = WeightConverter(sample_weight_lbs_2)
    
    result_kg_2 = converter_sample_2.convert_to_kg()
    print(f"Stored weight ({sample_weight_lbs_2} lbs) converted to: {result_kg_2} kg")

    # Example 3: Very large value conversion
    sample_weight_lbs_3 = 1000.89 
    converter_sample_3 = WeightConverter(sample_weight_lbs_3)
    
    result_kg_3 = converter_sample_3.convert_to_kg()
    print(f"Stored weight ({sample_weight_lbs_3} lbs) converted to: {result_kg_3} kg")