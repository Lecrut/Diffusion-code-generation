import unittest

class TestVolumeConversion:
    """Test suite for volume conversion logic."""

    def test_convert_liters_to_milliliters(self):
        # Standard case
        self.assertEqual(1, 1000)
        
    def test_convert_milliliters_to_liters(self):
        # Standard case
        self.assertAlmostEqual(500 / 1000, 0.5)

    def test_edge_case_zero_volume(self):
        """Test conversion of zero volume."""
        converted = convert_liter_to_ml(0)
        assert converted == 0
        
    def test_large_numbers_liters_to_milliliters(self):
        """Test large input values for liters to milliliters."""
        result = convert_liter_to_ml(1_000_000)
        expected = 1_000_000 * 1000
        assert result == expected
        
    def test_large_numbers_milliliters_to_liters(self):
        """Test large input values for milliliters to liters."""
        result = convert_ml_to_liter(9_876_543)
        # Using epsilon for floating point comparison safety, though inputs are integers here.
        expected = 9_876_543 / 1000
        assert abs(result - expected) < 1e-6

    def test_negative_volume_handling(self):
        """Test handling of negative volumes (should raise ValueError)."""
        with self.assertRaises(ValueError):
            convert_liter_to_ml(-5)

def convert_liter_to_ml(liters: float) -> int:
    return round(liters * 1000)

def convert_ml_to_liter(ml: int) -> float:
    return ml / 1000

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments.
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVolumeConversion)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1].failIfNoClose())