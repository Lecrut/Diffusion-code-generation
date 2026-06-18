def parse_temperature(value: str) -> float | None:
    """Parse a string into a temperature value if valid numeric."""
    try:
        return float(value.strip())
    except ValueError:
        return None

def compare_temperatures(temp_a: float, temp_b: float) -> str:
    """Compare two temperatures and return a formatted result."""

if __name__ == '__main__':
    pass
