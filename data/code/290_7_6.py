import unittest
class MassConverter:
    def convert_mass(self, mass, unit):
        if unit == "kg":
            return mass
        elif unit == "g":
            return mass / 1000.0
        elif unit == "mg":
            return mass / 1000000.0
        else:
            raise ValueError("Unsupported unit")
class TestMassConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MassConverter()
    def test_convert_kg(self):
        self.assertEqual(self.converter.convert_mass(10.5, "kg"), 10.5)
        self.assertEqual(self.converter.convert_mass(0.0, "kg"), 0.0)
        self.assertEqual(self.converter.convert_mass(1000.0, "kg"), 1000.0)
    def test_convert_g(self):
        self.assertEqual(self.converter.convert_mass(1000.0, "g"), 1.0)
        self.assertEqual(self.converter.convert_mass(500.5, "g"), 0.5005)
        self.assertEqual(self.converter.convert_mass(0.0, "g"), 0.0)
    def test_convert_mg(self):
        self.assertEqual(self.converter.convert_mass(1000000.0, "mg"), 1.0)
        self.assertEqual(self.converter.convert_mass(500000.0, "mg"), 0.5)
        self.assertEqual(self.converter.convert_mass(1234567.89, "mg"), 1.23456789)
        self.assertEqual(self.converter.convert_mass(0.0, "mg"), 0.0)
    def test_unsupported_unit(self):
        with self.assertRaisesRegex(ValueError, "Unsupported unit"):
            self.converter.convert_mass(10, "ton")
        with self.assertRaisesRegex(ValueError, "Unsupported unit"):
            self.converter.convert_mass(10, "gram")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)