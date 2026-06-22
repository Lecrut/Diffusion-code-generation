def convert_pints_to_quarts(pints):
    conversion_factor = 0.5
    return pints * conversion_factor

if __name__ == '__main__':
    sample_values = [4, 10, 20]
    for pints in sample_values:
        quarts = convert_pints_to_quarts(pints)
        print(f"{pints} pints is equal to {quarts} quarts")