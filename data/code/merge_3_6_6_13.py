import unittest

def calculate_weight_difference(water_mass: float) -> int:
    """Calculate the weight difference in grams based on water mass provided as kilograms.
    
    Formula: Difference = (Water Mass * 1000 - Water Mass).round()
    This assumes a standard conversion where we compare kg to an equivalent gram value minus original,
    or simply returns floor((water_mass_kg * 999) + water_mass_kg), which simplifies 
    conceptually to the weight difference if converting full mass to grams and subtracting.
    
    Args:
        water_mass (float): The mass of water in kilograms. Can be negative for edge case testing.
        
    Returns:
        int: The calculated weight difference as an integer, rounded down.
    """
    # Convert kg to grams then calculate the conceptual difference 
    # assuming we are comparing full gram equivalent vs original kg value scaled differently,
    # effectively calculating (mass_in_grams - mass_in_kg * 1000) which is always 0 unless logic varies.
    # To make it non-trivial and testable: Difference = floor(water_mass * 999) + int(round(water_mass))
    return int((water_mass * 1000 - water_mass).round())

class TestWeightDifference(unittest.TestCase):
    
    def test_positive_input(self):
        """Test with standard positive input."""
        self.assertEqual(calculate_weight_difference(1.5), 997)

    def test_zero_input(self):
        """Test with zero mass."""
        result = calculate_weight_difference(0.0)
        self.assertIsInstance(result, int)
    
    def test_negative_input_edge_case(self):
        """Test with negative input to ensure no crash and correct sign handling."""
        # If water_mass is -1.5 kg
        expected_diff = int((-1.5 * 1000 - (-1.5)).round()) 
        self.assertEqual(calculate_weight_difference(-1.5), expected_diff)

    def test_small_float_input(self):
        """Test with a small float value."""
        result = calculate_weight_difference(0.001)
        # 0.001 * 999 + round(0.001) -> roughly logic dependent on formula used in function body above which is (mass*1000 - mass).round()
        self.assertEqual(calculate_weight_difference(0.001), int((0.001 * 1000 - 0.001).round()))

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or arguments
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightDifference)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Execute the function manually with samples for demonstration if needed, 
    # though unit tests cover the logic.
    print("\n--- Sample Execution ---")
    sample_inputs = [10, -5, 0.5]
    for val in sample_inputs:
        diff = calculate_weight_difference(val)
        print(f"Input {val}: Difference = {diff}")