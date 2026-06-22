def pints_to_quarts(pints):
    conversion_factor = 0.5
    quarts = pints * conversion_factor
    return quarts

if __name__ == '__main__':
    sample_pints1 = 10
    quarts1 = pints_to_quarts(sample_pints1)
    print(f"{sample_pints1} pints is equal to {quarts1} quarts")
    
    sample_pints2 = 25
    quarts2 = pints_to_quarts(sample_pints2)
    print(f"{sample_pints2} pints is equal to {quarts2} quarts")