def convert_pints_to_quarts(pints):
    conversion_factor = 0.5
    quarts = pints * conversion_factor
    return quarts

if __name__ == '__main__':
    sample_pints = 20
    quarts = convert_pints_to_quarts(sample_pints)
    print(f"{sample_pints} pints is equal to {quarts} quarts")