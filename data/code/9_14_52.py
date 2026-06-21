def pints_to_quarts(pints):
    if pints < 0:
        raise ValueError("Volume cannot be negative")
    return pints / 2

if __name__ == '__main__':
    sample_pints = 10
    quarts = pints_to_quarts(sample_pints)
    print(f"{sample_pints} pints is equal to {quarts} quarts")