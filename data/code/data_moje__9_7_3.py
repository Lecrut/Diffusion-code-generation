import unittest

def convert_volume(volume: float, from_unit: str, to_unit: str) -> float:
    liters_per_unit = {'liter': 1.0, 'gallon': 3.78541, 'milliliter': 0.001, 'cup': 0.236588}
    if from_unit not in liters_per_unit:
        raise ValueError(f'Unknown source unit: {from_unit}')
    if to_unit not in liters_per_unit:
        raise ValueError(f'Unknown target unit: {to_unit}')
    if volume < 0:
        raise ValueError('Volume cannot be negative')
    liters = volume * liters_per_unit[from_unit]
    result = liters / liters_per_unit[to_unit]
    return result

class TestVolumeConversion(unittest.TestCase):

    def test_convert_liter_to_liter(self):
        self.assertAlmostEqual(convert_volume(5, 'liter', 'liter'), 5.0)

    def test_convert_gallon_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'liter'), 3.78541)

    def test_convert_liter_to_gallon(self):
        self.assertAlmostEqual(convert_volume(3.78541, 'liter', 'gallon'), 1.0)

    def test_convert_milliliter_to_liter(self):
        self.assertAlmostEqual(convert_volume(1000, 'milliliter', 'liter'), 1.0)

    def test_convert_liter_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'liter', 'milliliter'), 1000.0)

    def test_convert_cup_to_liter(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'liter'), 0.236588)

    def test_convert_zero_volume(self):
        self.assertEqual(convert_volume(0, 'liter', 'gallon'), 0.0)

    def test_convert_zero_volume_gallons(self):
        self.assertEqual(convert_volume(0, 'gallon', 'milliliter'), 0.0)

    def test_convert_large_number(self):
        result = convert_volume(1000000, 'milliliter', 'liter')
        self.assertAlmostEqual(result, 1000.0)

    def test_convert_negative_volume(self):
        with self.assertRaises(ValueError):
            convert_volume(-1, 'liter', 'gallon')

    def test_convert_unknown_source_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'barrel', 'liter')

    def test_convert_unknown_target_unit(self):
        with self.assertRaises(ValueError):
            convert_volume(1, 'liter', 'barrel')

    def test_convert_gallon_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'milliliter'), 3785.41)

    def test_convert_milliliter_to_gallon(self):
        self.assertAlmostEqual(convert_volume(3785.41, 'milliliter', 'gallon'), 1.0)

    def test_convert_cup_to_milliliter(self):
        self.assertAlmostEqual(convert_volume(1, 'cup', 'milliliter'), 236.588)

    def test_convert_milliliter_to_cup(self):
        self.assertAlmostEqual(convert_volume(236.588, 'milliliter', 'cup'), 1.0)

    def test_convert_gallon_to_cup(self):
        liters = 1 * 3.78541
        cups = liters / 0.236588
        self.assertAlmostEqual(convert_volume(1, 'gallon', 'cup'), cups)

    def test_convert_cup_to_gallon(self):
        liters = 1 * 0.236588
        gallons = liters / 3.78541
        self.assertAlmostEqual(convert_volume(1, 'cup', 'gallon'), gallons)
if __name__ == '__main__':
    sample_volume = 2.5
    source = 'liter'
    target = 'gallon'
    result = convert_volume(sample_volume, source, target)
    print(result)