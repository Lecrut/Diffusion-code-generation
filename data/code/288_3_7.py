CONVERSION_FACTOR = 4 / 5

def celsius_to_reaumur(celsius):
    return celsius * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_celsius = 0
    print(celsius_to_reaumur(sample_celsius))
    
    sample_celsius = 100
    print(celsius_to_reaumur(sample_celsius))
    
    sample_celsius = -40
    print(celsius_to_reaumur(sample_celsius))