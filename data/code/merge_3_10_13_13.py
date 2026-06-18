import sys

def parse_temperature(value: str) -> float | None:
    """Attempt to convert a string to a float."""
    try:
        return float(value.strip())
    except ValueError:
        return None

class TemperatureComparisonError(Exception):
    """Raised when temperature values are invalid or missing."""

    def __init__(self, message: str) -> None:
        super().__init__(message)

def compare_temperatures(temp_a: float | None, temp_b: float | None) -> tuple[str, bool]:
    """Compare two temperatures and return a formatted result string along with comparison status."""
    if not isinstance(temp_a, (int, float)) or not isinstance(temp_b, (int, float)):
        raise TemperatureComparisonError("Both temperature values must be numeric.")

if __name__ == '__main__':
    pass
