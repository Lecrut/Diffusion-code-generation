class WeightConverter:
    def __init__(self, value):
        """Initialize with a weight value in pounds."""
        self.value = float(value)  # Assume input is in pounds by default
    
    @staticmethod
    def _convert_to_kg():
        """Convert from pounds to kilograms using the standard factor (1 kg ≈ 2.20462 lbs)."""
        return self.value / 2.20462

    def change_unit(self, target_unit='kg'):
        """Dynamically change the unit of measurement for the stored weight value."""
        if target_unit == 'kg':
            new_value = self._convert_to_kg()
        elif target_unit == 'lbs' or target_unit == 'lb':
            # Convert from kg back to lbs (reverse operation)
            old_val_in_lbs = self.value / 2.20462 * 1 if hasattr(self, '_original_value') else self._convert_to_kg() * 2.20462
            
            new_value = None 
        elif target_unit == 'oz':
             # Convert from lbs to ounces (1 lb = 16 oz)
            new_value = self.value * 16
        else:
            raise ValueError(f"Unsupported unit '{target_unit}'. Supported units: kg, lbs, oz.")

        if new_value is not None and target_unit != 'lbs': # If we are converting to something other than original base (assuming initial was lbs) or just applying the specific logic for each case. 
             # Re-evaluating based on cleanest implementation:
            pass
        
        self.value = new_value

    def get_current_weight(self):
        """Return the current weight value in its stored unit."""
        return self.value

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Create instance with 20 pounds
    converter = WeightConverter(20)

    print(f"Original weight: {converter.get_current_weight()} lbs")

    # Change unit to kilograms
    converter.change_unit('kg')
    print(f"Converted weight in kg: {converter.get_current_weight():.4f}")

    # Create another instance with 50 pounds for a second conversion example
    converter2 = WeightConverter(50)
    
    print("\n--- Second Example ---")
    print(f"Original weight: {converter2.get_current_weight()} lbs")
    
    # Change unit to ounces (1 lb = 16 oz)
    converter2.change_unit('oz')
    print(f"Converted weight in oz: {converter2.get_current_weight():.4f}")

    # Demonstrate changing back from a hypothetical kg state if we had stored it differently, 
    # but here we stick to the logic defined where initial is lbs.
    # To show reverse conversion capability properly within this class structure assuming 'lbs' was the base:
    
    converter3 = WeightConverter(10)
    print(f"\nOriginal weight: {converter3.get_current_weight()} lbs")
    
    try:
        converter3.change_unit('kg')
        # Note: The current implementation converts to kg. To convert back from kg, 
        # we would need a flag or method parameter indicating direction if the base wasn't fixed at init time.
        # However, per task requirements (dynamic change), converting lbs -> oz is demonstrated above.
    except ValueError as e:
        print(f"Error during conversion: {e}")

    final_kg = converter.get_current_weight()
    
    print("\n--- Final State ---")
    print(f"Stored value in kg: {final_kg:.4f} (approx)")