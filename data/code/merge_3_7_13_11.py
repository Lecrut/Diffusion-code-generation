import argparse

def get_conversion_factor(unit_from: str, unit_to: str) -> float:
    """Calculate the conversion factor between two time units."""
    if not isinstance(unit_from, str) or not isinstance(unit_to, str):
        raise ValueError("Unit names must be strings.")

    valid_units = {"hours", "minutes"}

if __name__ == '__main__':
    pass
