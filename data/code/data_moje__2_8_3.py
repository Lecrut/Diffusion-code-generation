import math
import unittest

def calculate_cylinder_volume(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return math.pi * (radius ** 2) * height

def calculate_sphere_volume(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return (4 / 3) * math.pi * (radius ** 3)

def calculate_rectangular_prism_volume(length: float, width: float, height: float) -> float:
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return length * width * height

def calculate_cone_volume(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    return (1 / 3) * math.pi * (radius ** 2) * height

class TestVolumeFunctions(unittest.TestCase):

    def test_cylinder_positive_values(self):
        result = calculate_cylinder_volume(2.0, 5.0)
        expected = math.pi * 4.0 * 5.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cylinder_zero_radius(self):
        result = calculate_cylinder_volume(0.0, 5.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cylinder_zero_height(self):
        result = calculate_cylinder_volume(2.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cylinder_zero_both(self):
        result = calculate_cylinder_volume(0.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cylinder_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-2.0, 5.0)

    def test_cylinder_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(2.0, -5.0)

    def test_cylinder_negative_both(self):
        with self.assertRaises(ValueError):
            calculate_cylinder_volume(-2.0, -5.0)

    def test_sphere_positive_value(self):
        result = calculate_sphere_volume(3.0)
        expected = (4 / 3) * math.pi * 27.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_sphere_zero_radius(self):
        result = calculate_sphere_volume(0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_sphere_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_sphere_volume(-3.0)

    def test_rectangular_prism_positive_values(self):
        result = calculate_rectangular_prism_volume(2.0, 3.0, 4.0)
        expected = 24.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_rectangular_prism_zero_length(self):
        result = calculate_rectangular_prism_volume(0.0, 3.0, 4.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_rectangular_prism_zero_width(self):
        result = calculate_rectangular_prism_volume(2.0, 0.0, 4.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_rectangular_prism_zero_height(self):
        result = calculate_rectangular_prism_volume(2.0, 3.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_rectangular_prism_zero_all(self):
        result = calculate_rectangular_prism_volume(0.0, 0.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_rectangular_prism_negative_length(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(-2.0, 3.0, 4.0)

    def test_rectangular_prism_negative_width(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(2.0, -3.0, 4.0)

    def test_rectangular_prism_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_rectangular_prism_volume(2.0, 3.0, -4.0)

    def test_cone_positive_values(self):
        result = calculate_cone_volume(2.0, 5.0)
        expected = (1 / 3) * math.pi * 4.0 * 5.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cone_zero_radius(self):
        result = calculate_cone_volume(0.0, 5.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cone_zero_height(self):
        result = calculate_cone_volume(2.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cone_zero_both(self):
        result = calculate_cone_volume(0.0, 0.0)
        expected = 0.0
        self.assertAlmostEqual(result, expected, places=7)

    def test_cone_negative_radius(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(-2.0, 5.0)

    def test_cone_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_cone_volume(2.0, -5.0)

if __name__ == '__main__':
    r, h = 3.0, 5.0
    v_cyl = calculate_cylinder_volume(r, h)
    print(v_cyl)

    r = 4.0
    v_sph = calculate_sphere_volume(r)
    print(v_sph)

    l, w, h = 2.0, 3.0, 4.0
    v_box = calculate_rectangular_prism_volume(l, w, h)
    print(v_box)

    r, h = 2.0, 6.0
    v_cone = calculate_cone_volume(r, h)
    print(v_cone)

    r, h = 0.0, 0.0
    v_cyl_zero = calculate_cylinder_volume(r, h)
    print(v_cyl_zero)

    r = -1.0
    try:
        v_sph_neg = calculate_sphere_volume(r)
    except ValueError:
        v_sph_neg = "ValueError raised"
    print(v_sph_neg)