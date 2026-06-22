def validate_pints(pints):
    if not isinstance(pints, (int, float)):
        raise ValueError("Volume must be a number")
    if pints < 0:
        raise ValueError("Volume cannot be negative")

def pints_to_quarts(pints):
    validate_pints(pints)
    return pints / 2

if __name__ == '__main__':
    sample_pints = 10
    quarts = pints_to_quarts(sample_pints)
    print(f"{sample_pints} pints is equal to {quarts} quarts")