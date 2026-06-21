def validate_pints(pints):
    if not isinstance(pints, (int, float)):
        raise ValueError("Input must be a number")
    if pints < 0:
        raise ValueError("Volume cannot be negative")

def pints_to_quarts(pints):
    validate_pints(pints)
    return pints / 2

if __name__ == '__main__':
    sample_pints1 = 10
    quarts1 = pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")

    sample_pints2 = 20
    quarts2 = pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")