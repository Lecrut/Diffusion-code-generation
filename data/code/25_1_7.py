def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [0.0, -5, "0", [], {}, None]
    
    for item in samples:
        result = is_zero(item)
        print(f"is_zero({item!r}) -> {result}")