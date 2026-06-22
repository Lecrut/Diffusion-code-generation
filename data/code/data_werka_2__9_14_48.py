def pints_to_quarts(pints):
    if pints < 0:
        raise ValueError("Volume cannot be negative")
    return pints / 2

if __name__ == '__main__':
    sample_pints1 = 4
    quarts1 = pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")

    sample_pints2 = 10
    quarts2 = pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")