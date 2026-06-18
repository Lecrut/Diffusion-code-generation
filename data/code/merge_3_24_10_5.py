def is_negative(value):
    """Returns True if value is strictly less than zero, False otherwise."""
    return value < 0

if __name__ == '__main__':
    samples = [-5, -3.14, 0, 2]
    for s in samples:
        print(f"is_negative({s}) -> {is_negative(s)}")