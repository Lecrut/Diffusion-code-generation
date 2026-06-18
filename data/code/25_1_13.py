def is_zero(value):
    """Returns True if value is exactly zero, False otherwise."""
    return (value == 0)

if __name__ == '__main__':
    # Hard-coded sample values to test various numeric types and edge cases
    samples = [0, 0.0, -0.0, float('nan'), None]
    
    for val in samples:
        try:
            result = is_zero(val)
            print(f"is_zero({val!r}) -> {result}")
        except Exception as e:
            # Handle non-numeric or invalid comparison cases gracefully without breaking the module
            if not isinstance(val, (int, float)) and val != NotImplemented:
                continue 
            result = is_zero(val)
            print(f"is_zero({val!r}) -> {result}")