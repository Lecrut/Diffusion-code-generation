import unittest
class MassConverter:
    def convert_mass(self, mass_kg, unit):
        if unit == "kg":
            return mass_kg
        elif unit == "g":
            return mass_kg * 1000
        elif unit == "mg":
            return mass_kg * 1000000
        else:
            raise ValueError("Unsupported unit")
class TestMassConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MassConverter()
    def test_convert_kg_to_kg(self):
        self.assertEqual(self.converter.convert_mass(10.5, "kg"), 10.5)
        self.assertEqual(self.converter.convert_mass(0, "kg"), 0)
        self.assertEqual(self.converter.convert_mass(-5.2, "kg"), -5.2)
    def test_convert_kg_to_g(self):
        self.assertEqual(self.converter.convert_mass(1.0, "g"), 1000.0)
        self.assertEqual(self.converter.convert_mass(0.0, "g"), 0.0)
        self.assertEqual(self.converter.convert_mass(2.5, "g"), 2500.0)
    def test_convert_kg_to_mg(self):
        self.assertEqual(self.converter.convert_mass(1.0, "mg"), 1000000.0)
        self.assertEqual(self.converter.convert_mass(0.0, "mg"), 0.0)
        self.assertEqual(self.converter.convert_mass(0.001, "mg"), 1.0)
    def test_invalid_unit(self):
        with self.assertRaisesRegex(ValueError, "Unsupported unit"):
            self.converter.convert_mass(10, "ton")
        with self.assertRaisesRegex(ValueError, "Unsupported unit"):
            self.converter.convert_mass(5, "gram")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)