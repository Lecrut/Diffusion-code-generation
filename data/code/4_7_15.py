import unittest

class DistanceConverter:
    """A class to convert distances between different units."""

    def __init__(self, value_in_meters):
        self.value = value_in_meters  # Store internal value in meters

    @staticmethod
    def _miles_to_meters(miles) -> float:
        return miles * 1609.344

    @staticmethod
    def _kilometers_to_meters(kilometers) -> float:
        return kilometers * 1000

    @staticmethod
    def _feet_to_meters(feet) -> float:
        return feet * 0.3048

    @staticmethod
    def _yards_to_meters(yards) -> float:
        return yards * 0.9144

    @staticmethod
    def _miles_from_meters(meters) -> float:
        return meters / 1609.344

    @staticmethod
    def _kilometers_from_meters(meters) -> float:
        return meters / 1000

    @staticmethod
    def _feet_from_meters(meters) -> float:
        return meters / 0.3048

    @staticmethod
    def _yards_from_meters(meters) -> float:
        return meters / 0.9144

class TestDistanceConverter(unittest.TestCase):
    """Test suite for the DistanceConverter class."""

    # --- Conversion TO Meters Tests (Input from other units, Output in meters) ---

    def test_convert_from_miles_to_meters(self):
        converter = DistanceConverter(5.0)  # Input is treated as miles based on typical usage pattern if not specified otherwise, but here we assume the constructor accepts a specific unit or just value. 
        # To make this robust without external context of which unit was input, let's create explicit test cases for each conversion direction using static methods directly to ensure clarity.
        
    def setUp(self):
        self.converter_miles = DistanceConverter(10)  # Assuming first arg is miles if not specified otherwise in a real scenario, but here we will treat the constructor as accepting meters by default and provide specific test cases for conversions via public or private methods? 
        # Let's redefine logic slightly to be explicit:
        # Constructor takes value AND unit string.
        
    def __init__(self): pass

    def convert_to_miles(self, meters) -> float:
        return self._miles_from_meters(meters)

    def convert_to_kilometers(self, meters) -> float:
        return self._kilometers_from_meters(meters)

    def convert_to_feet(self, meters) -> float:
        return self._feet_from_meters(meters)

    def convert_to_yards(self, meters) -> float:
        return self._yards_from_meters(meters)

# Refined Class Structure for Clear Testing without Ambiguity
class DistanceConverter:
    """A class to handle distance conversions between miles, kilometers, feet, and yards."""

    # Constants
    METERS_PER_MILE = 1609.344
    METER_PER_KM = 1000
    FEET_PER_METER = 0.3048
    YARDS_PER_METER = 0.9144
    INVERSE_FOOT_PER_METER = 1 / 0.3048

    def __init__(self, value: float):
        """Initialize with a distance in meters."""
        self.value_meters = abs(value)

    # --- Conversion TO Meters (Inputs are other units) ---

    @staticmethod
    def miles_to_meters(miles: float) -> float:
        return DistanceConverter.METERS_PER_MILE * miles

    @staticmethod
    def kilometers_to_meters(kilometers: float) -> float:
        return DistanceConverter.METER_PER_KM * kilometers

    @staticmethod
    def feet_to_meters(feet: float) -> float:
        return DistanceConverter.FEET_PER_METER * feet

    @staticmethod
    def yards_to_meters(yards: float) -> float:
        return DistanceConverter.YARDS_PER_METER * yards

    # --- Conversion FROM Meters (Outputs are other units) ---

    @classmethod
    def meters_to_miles(cls, meters: float) -> float:
        return cls.meters / cls.METERS_PER_MILE

    @classmethod
    def meters_to_kilometers(cls, meters: float) -> float:
        return cls.meters / cls.METER_PER_KM

    @classmethod
    def meters_to_feet(cls, meters: float) -> float:
        # Using inverse for precision or direct division? Direct is fine here.
        return DistanceConverter.INVERSE_FOOT_PER_METER * meters if hasattr(DistanceConverter, 'INVERSE_FOOT_PER_METER') else (meters / 0.3048)

    @classmethod
    def meters_to_yards(cls, meters: float) -> float:
        # Using inverse for precision or direct division? Direct is fine here.
        return DistanceConverter.INVERSE_YARDS_PER_METER * meters if hasattr(DistanceConverter, 'INVERSE_YARDS_PER_METER') else (meters / 0.9144)

    @classmethod
    def _inverse_yards_per_meter(cls):
        # Calculate on fly to avoid class attribute dependency issues in static methods
        return cls.METERS_PER_KM * 3280.84 / 1609.344 # Approximation? No, let's just use the constant defined earlier but ensure it exists or calculate directly.
        # Actually, simpler: meters_to_yards = meters / (meters_per_meter) where meter_per_meter is yards per meter? 
        # 1 yard = 0.9144 meters -> 1 meter = 1/0.9144 yards.
        return cls.meters / 0.9144

# Final Clean Implementation for Testing
class DistanceConverter:
    """A class to handle distance conversions between miles, kilometers, feet, and yards."""

    # Constants defined as static methods or attributes for clarity in unit tests
    
    def __init__(self):
        pass

    @staticmethod
    def meters_to_miles(meters) -> float:
        return meters / 1609.344

    @staticmethod
    def miles_to_meters(miles) -> float:
        return miles * 1609.344

    @staticmethod
    def kilometers_to_meters(kilometers) -> float:
        return kilometers * 1000

    @staticmethod
    def meters_to_kilometers(meters) -> float:
        return meters / 1000

    @staticmethod
    def feet_to_meters(feet) -> float:
        return feet * 0.3048

    @staticmethod
    def meters_to_feet(meters) -> float:
        # Using inverse of the conversion factor for better precision in some contexts, 
        # though direct division is mathematically equivalent here.
        if meters == 0:
            return 0.0
        return meters / 0.3048

    @staticmethod
    def yards_to_meters(yards) -> float:
        return yards * 0.9144

    @staticmethod
    def meters_to_yards(meters) -> float:
        if meters == 0:
            return 0.0
        return meters / 0.9144

class TestDistanceConverter(unittest.TestCase):
    """Comprehensive test suite for the DistanceConverter class."""

    # --- Tests for miles conversions ---
    
    def test_miles_to_meters_exact(self):
        self.assertAlmostEqual(DistanceConverter.miles_to_meters(5), 8046.72, places=1)
        
    def test_miles_to_meter_negative(self):
        result = DistanceConverter.miles_to_meters(-3.5)
        expected = -3.5 * 1609.344
        self.assertAlmostEqual(result, expected, places=1)

    # --- Tests for kilometers conversions ---

    def test_kilometers_to_meters_exact(self):
        self.assertEqual(DistanceConverter.kilometers_to_meters(2), 2000)

    def test_kilometers_to_meter_negative(self):
        result = DistanceConverter.kilometers_to_meters(-1.5)
        expected = -1.5 * 1000
        self.assertAlmostEqual(result, expected, places=1)

    # --- Tests for feet conversions ---

if __name__ == '__main__':
    pass
