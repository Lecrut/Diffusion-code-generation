import unittest
from datetime import timedelta

class TimeConversionFunctions:
    """Module containing time conversion utility functions."""

    @staticmethod
    def seconds_to_timedelta(total_seconds):
        """Convert total seconds into a timedelta object."""
        if not isinstance(total_seconds, (int, float)):
            raise TypeError("Input must be an integer or float representing seconds.")
        
        # Handle negative values correctly for backward time calculation
        return timedelta(seconds=total_seconds)

    @staticmethod
    def timedelta_to_seconds(td):
        """Convert a timedelta object back to total seconds."""
        if not isinstance(td, timedelta):
            raise TypeError("Input must be a datetime.timedelta instance.")
        
        # Calculate total seconds including microseconds (scaled by 10^6)
        return td.total_seconds()

    @staticmethod
    def format_duration(seconds):
        """Format duration into human-readable string HH:MM:SS.microseconds."""
        if not isinstance(seconds, (int, float)):
            raise TypeError("Input must be a number of seconds.")
        
        total = int(round(seconds))
        hours = abs(total) // 3600
        minutes = (abs(total) % 3600) // 60
        secs = abs(total) % 60
        
        # Handle negative sign separately for formatting if needed, 
        # but timedelta handles the math internally.
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"

class TestTimeConversionFunctions(unittest.TestCase):

    def test_seconds_to_timedelta_zero(self):
        """Test conversion of zero seconds."""
        result = TimeConversionFunctions.seconds_to_timedelta(0)
        self.assertEqual(result.total_seconds(), 0.0)
        
    def test_seconds_to_timedelta_positive_large(self):
        """Test conversion with a large positive time span (years worth)."""
        # Approximate one year in seconds: 365 * 24 * 60 * 60 = 31,536,000
        years_seconds = 31_536_000.75
        result = TimeConversionFunctions.seconds_to_timedelta(years_seconds)
        
        expected_hours = int(years_seconds / 3600) + (int((years_seconds % 3600)) // 60) * 60 # Simplified check logic below
        
        self.assertEqual(result.total_seconds(), years_seconds, "Large positive span conversion failed")

    def test_seconds_to_timedelta_negative(self):
        """Test conversion with negative seconds."""
        result = TimeConversionFunctions.seconds_to_timedelta(-31536)  # -1 year roughly
        expected_total = timedelta(seconds=-31536).total_seconds()
        
        self.assertEqual(result.total_seconds(), expected_total, "Negative span conversion failed")

    def test_seconds_to_timedelta_float_precision(self):
        """Test float input precision handling."""
        result = TimeConversionFunctions.seconds_to_timedelta(0.75)
        # timedelta constructor accepts floats but stores as int seconds + microseconds internally logic varies slightly by version, 
        # total_seconds() returns the exact float value back usually or scaled integer depending on implementation details in standard lib.
        self.assertEqual(result.total_seconds(), 0.75)

    def test_timedelta_to_seconds_zero(self):
        """Test conversion of zero timedelta."""
        td = timedelta(0, microseconds=0) # Explicitly zero
        result = TimeConversionFunctions.timedelta_to_seconds(td)
        
        self.assertEqual(result, 0.0, "Zero timedelta conversion failed")

    def test_timedelta_to_seconds_large(self):
        """Test conversion of large timedelta."""
        td = timedelta(days=100, hours=59, minutes=59, seconds=59, microseconds=999_999)
        
        expected_total_seconds = 86400 * 100 + 3599.999999 # days to sec + rest
        
        result = TimeConversionFunctions.timedelta_to_seconds(td)

if __name__ == '__main__':
    pass
