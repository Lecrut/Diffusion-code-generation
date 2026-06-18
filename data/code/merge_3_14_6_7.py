import sys

def parse_volume(value):
    """Attempt to parse a string as a float."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid numeric value: '{value}'")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    vol_a_str = "250"
    vol_b_str = "300"

    try:
        volume_a = parse_volume(vol_a_str)
        volume_b = parse_volume(vol_b_str)
        
        if volume_a < volume_b:
            print(f"{volume_a} is less than {volume_b}")
        elif volume_a > volume_b:
            print(f"{volume_a} is greater than {volume_b}")
        else:
            print(f"{volume_a} equals {volume_b}")
    except ValueError as e:
        # This block handles the case where parsing fails, though 
        # with hard-coded strings it will not be triggered.
        raise Exception("Validation Error") from e