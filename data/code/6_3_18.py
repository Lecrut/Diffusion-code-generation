def parse_weight(value: str) -> float:
    """Converts a string weight value to a float."""
    try:
        return float(value.strip())
    except ValueError as e:
        raise TypeError(f"Invalid weight input '{value}': {e}") from None

if __name__ == '__main__':
    # Hard-coded sample values for testing (no user interaction)
    SAMPLE_WEIGHT_1 = "65.0"
    SAMPLE_WEIGHT_2 = "70.5"

    try:
        weight_a_str = str(SAMPLE_WEIGHT_1)
        weight_b_str = str(SAMPLE_WEIGHT_2)

        # Validate inputs by attempting conversion directly to catch errors early if needed, 
        # though we proceed assuming valid strings as per sample requirement.
        
        weight_a = parse_weight(weight_a_str)
        weight_b = parse_weight(weight_b_str)
        
        difference = weight_b - weight_a
        
        print(f"{difference:.2f}")

    except TypeError:
        # This block handles the case where non-numeric strings are used in a real scenario.
        # Since samples are valid floats, this won't trigger with current code logic above, 
        # but ensures robustness if input validation were stricter or inputs changed later.
        pass