import sys

def parse_volume(value: str) -> float | None:
    """Attempts to convert a string representation of a number to a float."""
    try:
        return float(value.strip())
    except ValueError:
        return None

def compare_volumes(vol_a: float, vol_b: float) -> tuple[int]:
    """Compares two volume measurements and returns comparison codes.

    Returns:
        A tuple (result_code, message).
        
    Codes:
        0 if volumes are equal.
        -1 if first is less than second.
        1 if first is greater than second.
    """

if __name__ == '__main__':
    pass
