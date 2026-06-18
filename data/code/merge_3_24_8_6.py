def is_negative(value):
    """Returns True if value < 0, False otherwise."""
    return value < 0

if __name__ == '__main__':
    test_values = [ -5, 10 ]
    
    for val in test_values:
        negative_status = "negative" if is_negative(val) else "not negative (non-negative)"
        print(f"The number {val} is considered {negative_status}.")