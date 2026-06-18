import argparse
from decimal import Decimal, InvalidOperation

def parse_volume(value: str) -> float:
    """Parse a string into a floating-point number."""
    try:
        return float(Decimal(value))
    except (InvalidOperation, ValueError):
        raise argparse.ArgumentTypeError(f"Invalid volume value: '{value}'")

class VolumeConverter:
    def __init__(self, input_unit: str, output_unit: str):
        self.input_unit = input_unit.lower()
        self.output_unit = output_unit.lower()

        # Define conversion factors to liters (base unit) and then to target

if __name__ == '__main__':
    pass
