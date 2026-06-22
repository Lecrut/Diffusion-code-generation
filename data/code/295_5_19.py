CONVERSION_FACTOR = 2.54

def inches_to_cm(inches):
    return inches * CONVERSION_FACTOR

if __name__ == '__main__':
    sample_inches = 10
    print(f"Conversion factor from inches to centimeters: {inches_to_cm(1)} cm")